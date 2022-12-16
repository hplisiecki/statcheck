from Python.file_to_txt import getPDF
from Python.statcheck import statcheck
from Python.checkdir import checkPDF, checkPDFdir
from Python.summary_statcheck import summary_statcheck
import warnings

warnings.filterwarnings("ignore")

dir = r'D:\data\ranking\swps'
subdir = False


file = r'D:\GitHub\statcheck\pdfs\Agata_Dębowska_18.pdf'
#
texts = getPDF([file])
# #
Res, pRes = statcheck(texts)

# Res, pRes = statcheck("blablabla the effect was very significant (t(48) = 1.02, p < .05)")

Res, pRes = checkPDFdir(r'D:\data\ranking\swps', subdir = False)

res = summary_statcheck(Res)

