import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from isni_validation_claim_audit.audit import audit, claims, evidence, main
from isni_validation_claim_audit.phrases import ISNIVALIDATION, NOISNIVALIDATION, GENERIC_NAMES

class AuditTests(unittest.TestCase):
    def test_phrases(self):
        for phrase in ISNIVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NOISNIVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate isni\n```'), (False, False))
        self.assertEqual(claims("doesn't validate isni"), (False, True))
    def test_library_routes(self):
        for method in ('validate', 'is_valid'):
            for source in ('import stdnum.isni\nstdnum.isni.%s(x)', 'import stdnum.isni as s\ns.%s(x)', 'import stdnum\nstdnum.isni.%s(x)', 'from stdnum import isni as s\ns.%s(x)', 'from stdnum.isni import %s as f\nf(x)'):
                with self.subTest(source=source, method=method): self.assertTrue(evidence(source % method))
        for source in ('import idutils\nidutils.is_isni(x)', 'import idutils as i\ni.is_isni(x)', 'from idutils import is_isni\nis_isni(x)', 'from idutils import is_isni as i\ni(x)', 'from idutils.validators import is_isni\nis_isni(x)'):
            with self.subTest(source=source): self.assertTrue(evidence(source))
    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            with self.subTest(name=name):
                self.assertTrue(evidence('obj.%s(x)' % name))
                self.assertTrue(evidence('from lib import %s as f\nf(x)' % name))
                self.assertFalse(evidence('%s(x)' % name))
                self.assertFalse(evidence('def %s(x): pass\nobj.%s(x)' % (name, name)))
        self.assertTrue(evidence('result = thing()\nresult.validate_isni(x)'))
    def test_not_evidence(self):
        cases = ['import idutils', 'import stdnum.isni', 'is_isni(x)', 'validate(x)', 'is_valid(x)', 'compact(x)', 'format(x)', 'validate_isni(x)', 'obj.is_isni(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'obj.compact(x)', 'obj.format(x)', 'import idutils\nidutils.normalize_orcid(x)', 'import stdnum.isni\nstdnum.isni.compact(x)', 'import stdnum.isni\nstdnum.isni.format(x)', 'from stdnum.iso7064 import mod_11_2\nmod_11_2.calc_check_digit(x)', 'from stdnum.iso7064 import mod_11_2\nmod_11_2.validate(x)', 'import idutils\nidutils.detect_identifier_schemes(x)', 'api.get(x)', 'import idutils\nidutils.is_orcid(x)', 'import re\nre.match("x", x)', 'import re\nre.search("x", x)', 'import re\nre.fullmatch("x", x)', 'len(x) == 16', 'x[4] == "-"', 'x.isdigit()', 'obj.lookup_isni(x)', 'obj.generate_isni()', '"validate isni"', '# isni validation', 'validate_isni', 'def broken(', 'import subprocess\nsubprocess.run(["checker", x])', 'import stdnum.isni as s\ns = x\ns.validate(x)', 'from stdnum.isni import validate\ndef validate(x): pass\nvalidate(x)', 'import idutils as i\nwith thing() as i: pass\ni.is_isni(x)']
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))
    def test_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'README.md').write_text('validate isni')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'tests').mkdir()
            (root / 'tests/test_x.py').write_text('import idutils\nidutils.is_isni(x)')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')
            (root / 'app.py').write_text('import stdnum.isni\nstdnum.isni.is_valid(x)')
            self.assertEqual(audit(root), [])
            (root / 'README.md').write_text('no isni validation')
            self.assertEqual(audit(root)[0]['id'], 'documented-no-isni-validation-claim-false')
            self.assertEqual(audit(root, ['app.py']), [])
    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(['audit', tmp, '--json']), 0)
            self.assertEqual(main(['audit', tmp, '--fail-on', 'medium']), 0)
            self.assertEqual(main(['audit', tmp + '/missing']), 1)
