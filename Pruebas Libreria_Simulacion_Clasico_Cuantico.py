# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/21

# Pruebas de la Librería Simulación de lo Clásico a lo Cuántico

from Libreria_Simulacion_Clasico_Cuantico import *
import unittest as ut

class Test_Libreria_Nombre(ut.TestCase):
    
    def test_Sim_Exp_Can_Det(self):
        """Prueba del cálculo de la simulación del experimento determinístico de canicas
        None -> OK or FAILED (failures=#)"""
        xf = list(Sim_Exp_Can_Det_Prob_Cuan([[1,0,0,1], [0,0,1,0], [0,0,0,0], [0,1,0,0]], [0,1,3,2], 3))
        self.assertEqual(xf,[6,0,0,0])
        xf = list(Sim_Exp_Can_Det_Prob_Cuan([[0,0,0,1,0], [0,0,0,0,1], [1,0,1,0,0], [0,1,0,0,0], [0,0,0,0,0]], [1,0,1,0,1], 5))
        self.assertEqual(xf,[0,0,3,0,0])
        xf = list(Sim_Exp_Can_Det_Prob_Cuan([[0,1/6,5/6], [1/3,1/2,1/6], [2/3,1/3,0]], [2,0,1],2))
        self.assertEqual(xf,[1.25, 0.9166666666666666, 0.8333333333333333])
        xf = list(Sim_Exp_Can_Det_Prob_Cuan([[1/sqrt(2),1/sqrt(2),0], [1j/sqrt(2),-1j/sqrt(2),0], [0,0,1j]],[1,2,3],4))
        self.assertEqual(xf,[(1.4999999999999996+1.4999999999999996j), (0.4999999999999999-0.4999999999999999j), 3])
    
     
    def test_Sim_Exp_Ren_Part_Prob(self):
        """Prueba del cálculo de la simulación del experimento probabilístico de partículas
        None -> OK or FAILED (failures=#)"""
        m2,xf = Sim_Exp_Ren_Part_Prob(2,[[0,0,0,0,0,0,0,0], [1/2,0,0,0,0,0,0,0], [1/2,0,0,0,0,0,0,0],\
                                [0,1/3,0,1,0,0,0,0], [0,1/3,0,0,1,0,0,0], [0,1/3,1/3,0,0,1,0,0], [0,0,1/3,0,0,0,1,0],\
                                [0,0,1/3,0,0,0,0,1]])
        m2,xf = [list(x) for x in m2],[list(x) for x in xf]
        self.assertEqual(m2,[[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],\
                        [0.16666666666666666,0.3333333333333333,0,1,0,0,0,0], [0.16666666666666666,0.3333333333333333,0,0,1,0,0,0],\
                        [0.3333333333333333,0.3333333333333333,0.3333333333333333,0,0,1,0,0], [0.16666666666666666,0,0.3333333333333333,0,0,0,1,0],\
                        [0.16666666666666666,0,0.3333333333333333,0,0,0,0,1]])
        self.assertEqual(xf,[[0], [0], [0], [0.16666666666666666], [0.16666666666666666], [0.3333333333333333], [0.16666666666666666], [0.16666666666666666]])
        
        
    def test_Sim_Exp_Ren_Part_Cuan(self):
        """Prueba del cálculo de la simulación del experimento cuántico de partículas
        None -> OK or FAILED (failures=#)"""
        m2,xf = Sim_Exp_Ren_Part_Cuan(2,[[0,0,0,0,0,0,0,0], [1/sqrt(2),0,0,0,0,0,0,0], [1/sqrt(2),0,0,0,0,0,0,0],\
                                [0,(-1+1j)/sqrt(6),0,1,0,0,0,0], [0,(-1-1j)/sqrt(6),0,0,1,0,0,0], [0,(1-1j)/sqrt(6),(-1+1j)/sqrt(6),0,0,1,0,0],\
                                [0,0,(-1-1j)/sqrt(6),0,0,0,1,0], [0,0,(1-1j)/sqrt(6),0,0,0,0,1]])
        m2,xf = [list(x) for x in m2],[list(x) for x in xf]
        self.assertEqual(m2,[[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],\
                        [(-0.2886751345948129+0.2886751345948129j),(-0.4082482904638631+0.4082482904638631j),0,1,0,0,0,0],\
                        [(-0.2886751345948129-0.2886751345948129j),(-0.4082482904638631-0.4082482904638631j),0,0,1,0,0,0],\
                        [(2.4514267852689627e-17-2.4514267852689627e-17j),(0.4082482904638631-0.4082482904638631j),(-0.4082482904638631+0.4082482904638631j),0,0,1,0,0],\
                        [(-0.2886751345948129-0.2886751345948129j),0,(-0.4082482904638631-0.4082482904638631j),0,0,0,1,0],\
                        [(0.2886751345948129-0.2886751345948129j),0,(0.4082482904638631-0.4082482904638631j),0,0,0,0,1]])
        self.assertEqual(xf,[[0],[0],[0],[(-0.2886751345948129+0.2886751345948129j)],[(-0.2886751345948129-0.2886751345948129j)],\
                        [(2.4514267852689627e-17-2.4514267852689627e-17j)],[(-0.2886751345948129-0.2886751345948129j)],[(0.2886751345948129-0.2886751345948129j)]])


if __name__ == '__main__':
    ut.main()