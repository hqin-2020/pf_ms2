import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing
import seaborn as sns
import time
from pa import *
from tqdm import tqdm
import pickle
import os
sns.set()

if __name__ == '__main__':
    workdir = os.path.dirname(os.getcwd())
    srcdir = os.getcwd()
    datadir = workdir + '/data/'
    outputdir = workdir + '/output/'
    docdir = workdir + '/doc/'

    obs_series = pd.read_csv(datadir + 'data.csv', delimiter=',')
    obs_series = np.array(obs_series.iloc[:,1:]).T

    T = obs_series.shape[1]
    N = 100_000
    batch_num = 151

    θ_name = ['λ', 'η', \
            'b11', 'b22', \
            'As11', 'As12', 'As13',\
            'As21', 'As22', 'As23', 'Aso2', \
            'As31', 'As32', 'As33', 'Aso3', \
            'Bs11', 'Bs21', 'Bs22', 'Bs31', 'Bs32', 'Bs33',\
            'j21',  'j31',  'j32']

    def return_dir(seed):
        case = 'actual data, seed = ' + str(seed) + ', T = ' + str(T) + ', N = ' + str(N)
        return outputdir + case  + '/'

    casedir = []
    for i in range(batch_num):
        casedir.append(return_dir(i))

    t = 282
    θ_final = []
    success_seed = []
    for i in tqdm(range(1,batch_num)):
        try:
            with open(casedir[i] + 'θ_'+str(t)+'.pkl', 'rb') as f:
                θ_final.append(pickle.load(f))
            success_seed.append(i)
        except:
            pass

    def return_coll(θ_final):
        λ_particle = []; η_particle = []; b11_particle = []; b22_particle = []
        As11_particle = []; As12_particle = []; As13_particle = []; 
        As21_particle = []; As22_particle = []; As23_particle = []; Aso2_particle = []
        As31_particle = []; As32_particle = []; As33_particle = []; Aso3_particle = []
        Bs11_particle = []; Bs21_particle = []; Bs22_particle = []; Bs31_particle = []; Bs32_particle = []; Bs33_particle = []
        j21_particle = []; j31_particle = []; j32_particle = [];
        λ_iter_particle = []; Ass_iter_particle = []

        for n in range(N):
            λ_particle.append(θ_final[n][1][1,1])
            η_particle.append(θ_final[n][0][1,0])
            b11_particle.append(θ_final[n][2][0,0])
            b22_particle.append(θ_final[n][2][1,1])
            As11_particle.append(θ_final[n][4][0,0])
            As12_particle.append(θ_final[n][4][0,1])
            As13_particle.append(θ_final[n][4][0,2])
            As21_particle.append(θ_final[n][4][1,0])
            As22_particle.append(θ_final[n][4][1,1])
            As23_particle.append(θ_final[n][4][1,2])
            Aso2_particle.append(θ_final[n][3][1,0])
            As31_particle.append(θ_final[n][4][2,0])
            As32_particle.append(θ_final[n][4][2,1])
            As33_particle.append(θ_final[n][4][2,2])
            Aso3_particle.append(θ_final[n][3][2,0])
            Bs11_particle.append(θ_final[n][5][0,0])
            Bs21_particle.append(θ_final[n][5][1,0])
            Bs22_particle.append(θ_final[n][5][1,1])
            Bs31_particle.append(θ_final[n][5][2,0])
            Bs32_particle.append(θ_final[n][5][2,1])
            Bs33_particle.append(θ_final[n][5][2,2])
            j21_particle.append(θ_final[n][6][1,0])
            j31_particle.append(θ_final[n][6][2,0])
            j32_particle.append(θ_final[n][6][2,1])
            λ_iter_particle.append(θ_final[n][7])
            Ass_iter_particle.append(θ_final[n][7])

        θ_coll = [λ_particle, η_particle, b11_particle, b22_particle, \
                As11_particle, As12_particle, As13_particle,\
                As21_particle, As22_particle, As23_particle, Aso2_particle,\
                As31_particle, As32_particle, As33_particle, Aso3_particle,\
                Bs11_particle, Bs21_particle, Bs22_particle, Bs31_particle, Bs32_particle, Bs33_particle,\
                j21_particle, j31_particle, j32_particle]
        return θ_coll

    θ_coll = []
    indexes = []
    for i in tqdm(range(len(θ_final))):
        θ_coll.append(return_coll(θ_final[i]))
        indexes.append('seed = '+str(success_seed[i]))

    Input = []
    for i in tqdm(range(len(θ_name))):
        Input.append([θ_coll,i])

    pool = multiprocessing.Pool()
    θ_all = pool.map(particle_append, tqdm(Input))

    for i in tqdm(range(len(θ_all))): 
        with open(outputdir + 'θ_all_' + str(θ_all[i][0]) + '.pkl', 'wb') as f:
                pickle.dump(θ_all[i], f)
