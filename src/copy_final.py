import shutil
import os
from tqdm import tqdm

workdir = os.path.dirname(os.getcwd())
source_dir = '/project2/lhansen/pf_ms2/'
destination_dir = workdir + '/output/'

N = 100_000
T = 283
batch_num = 150

for i in tqdm(range(150,151)):
    case = 'actual data, seed = ' + str(i) + ', T = ' + str(T) + ', N = ' + str(N)
    casedir = destination_dir + case  + '/'
    try:
        os.mkdir(casedir)
        shutil.copy(source_dir + case  + '/θ_50.pkl', casedir)
        shutil.copy(source_dir + case  + '/θ_100.pkl', casedir)
        shutil.copy(source_dir + case  + '/θ_200.pkl', casedir)
        shutil.copy(source_dir + case  + '/θ_282.pkl', casedir)
    except:
        pass
