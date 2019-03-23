"""creating pin codes from narrow chain complex
"""
import numpy as np
import QuantumCodeConstruction.pincode as pinco
from QuantumCodeConstruction.utils import writesparsematrix


if __name__ == "__main__":
    D = 7
    X = int(D/3)
    Z = D-X
    SIZE = 2
    # print('Generating narrow Pin Code with D={}, x={}, z={}, q={}'.format(D, X, Z, SIZE))
    # TRANSITIONS = [np.ones((SIZE, SIZE), dtype='uint8') for _ in range(D)]
    print('Narrow pin code 3-3-3-3-3-3-3-3')
    M33 = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]], dtype='uint8')
    TRANSITIONS = [M33,
                   np.ones((3, 3), dtype='uint8'),
                   M33,
                   np.ones((3, 3), dtype='uint8'),
                   M33,
                   np.ones((3, 3), dtype='uint8'),
                   M33]
    POSETHP = pinco.GrPoset(TRANSITIONS, iscomplete=False)
    PCX, PCZ = pinco.pincode(POSETHP, X, Z)
    WEIGHTSX = {a for che in PCX.sum(axis=1).tolist() for a in che}
    WEIGHTSZ = {a for che in PCZ.sum(axis=1).tolist() for a in che}
    print(WEIGHTSX)
    print(WEIGHTSZ)
    print(POSETHP.levelsizes)
    PCCHECKSX, PCQUBITS = PCX.shape
    PCCHECKSZ, _ = PCZ.shape
    print('qubits - xchecks - zchecks = logicals: \n \
           {} - {} - {} = {}'.format(PCQUBITS,
                                     PCCHECKSX,
                                     PCCHECKSZ,
                                     PCQUBITS - PCCHECKSX - PCCHECKSZ))

    CSSCOND = (np.dot(PCX.todense(), PCZ.transpose().todense()) % 2).sum() == 0
    print('This is a valid CSS code: {}'.format(CSSCOND))

    writesparsematrix(PCX, 'PCMatrices/narrowCC/narrowCC_33333333_dim{}_X.sms'.format(D))
    writesparsematrix(PCZ, 'PCMatrices/narrowCC/narrowCC_33333333_dim{}_Z.sms'.format(D))
