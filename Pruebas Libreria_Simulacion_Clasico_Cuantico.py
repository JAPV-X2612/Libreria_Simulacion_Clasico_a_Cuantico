# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / #xx Semestre
# Asignatura: [Nombre] (XXXX) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: ----/--/--

# Pruebas de la Librería [Nombre]

from Libreria_Simulacion_Clasico_Cuantico import *
import unittest as ut

class Test_Libreria_Nombre(ut.TestCase):
    
    def test_Sim_Exp_Can_Det(self):
        """Prueba del cálculo de la simulación del experimento determinístico de canicas
        None -> OK or FAILED (failures=#)"""
        xf = list(Sim_Exp_Can_Det([[1,0,0,1],[0,0,1,0],[0,0,0,0],[0,1,0,0]],[0,1,3,2],3))
        self.assertEqual(xf,[6,0,0,0])
        xf = list(Sim_Exp_Can_Det([[0,0,0,1,0],[0,0,0,0,1],[1,0,1,0,0],[0,1,0,0,0],[0,0,0,0,0]],[1,0,1,0,1],5))
        self.assertEqual(xf,[0,0,3,0,0])
    
     
    def test_Sim_Exp_Can_Det(self):
        """Prueba del cálculo de la simulación del experimento probabilístico de partículas
        None -> OK or FAILED (failures=#)"""
        m2,xf = Sim_Exp_Part_Prob(2,[[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],\
                                [0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],\
                                [0,0,1/3,0,0,0,0,1]])
        m2,xf = [list(x) for x in m2],[list(x) for x in xf]
        self.assertEqual(m2,[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],\
                        [0.16666666666666666,0.3333333333333333,0,1,0,0,0,0],[0.16666666666666666,0.3333333333333333,0,0,1,0,0,0],\
                        [0.3333333333333333,0.3333333333333333,0.3333333333333333,0,0,1,0,0],[0.16666666666666666,0,0.3333333333333333,0,0,0,1,0],\
                        [0.16666666666666666,0,0.3333333333333333,0,0,0,0,1]])
        self.assertEqual(xf,[[0],[0],[0],[0.16666666666666666],[0.16666666666666666],[0.3333333333333333],[0.16666666666666666],[0.16666666666666666]])
        
        
    def test_Sim_Exp_Part_Cuan(self):
        """Prueba del cálculo de la simulación del experimento cuántico de partículas
        None -> OK or FAILED (failures=#)"""
        m2,xf = Sim_Exp_Part_Cuan(2,[[0,0,0,0,0,0,0,0],[1/sqrt(2),0,0,0,0,0,0,0],[1/sqrt(2),0,0,0,0,0,0,0],\
                                [0,(-1+1j)/sqrt(6),0,1,0,0,0,0],[0,(-1-1j)/sqrt(6),0,0,1,0,0,0],[0,(1-1j)/sqrt(6),(-1+1j)/sqrt(6),0,0,1,0,0],\
                                [0,0,(-1-1j)/sqrt(6),0,0,0,1,0],[0,0,(1-1j)/sqrt(6),0,0,0,0,1]])
        m2,xf = [list(x) for x in m2],[list(x) for x in xf]
        self.assertEqual(m2,[[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],\
                        [(-0.2886751345948129+0.2886751345948129j),(-0.4082482904638631+0.4082482904638631j),0,1,0,0,0,0],\
                        [(-0.2886751345948129-0.2886751345948129j),(-0.4082482904638631-0.4082482904638631j),0,0,1,0,0,0],\
                        [(2.4514267852689627e-17-2.4514267852689627e-17j),(0.4082482904638631-0.4082482904638631j),(-0.4082482904638631+0.4082482904638631j),0,0,1,0,0],\
                        [(-0.2886751345948129-0.2886751345948129j),0,(-0.4082482904638631-0.4082482904638631j),0,0,0,1,0],\
                        [(0.2886751345948129-0.2886751345948129j),0,(0.4082482904638631-0.4082482904638631j),0,0,0,0,1]])
        self.assertEqual(xf,[[0],[0],[0],[(-0.2886751345948129+0.2886751345948129j)],[(-0.2886751345948129-0.2886751345948129j)],\
                        [(2.4514267852689627e-17-2.4514267852689627e-17j)],[(-0.2886751345948129-0.2886751345948129j)],[(0.2886751345948129-0.2886751345948129j)]])


if __name__ == '__main__':
    ut.main()