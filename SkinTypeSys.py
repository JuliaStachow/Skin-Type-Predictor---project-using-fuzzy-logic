import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class FuzzyModel:
    def __init__(self):
        self.acne_frequency = None
        self.resistance = None
        self.skin_type = None
        self.baking_ctrl = None
        self.braking_ctrl_simulation = None

    def perform_fuzzy_logic(self, input1, input2):
        self.acne_frequency = ctrl.Antecedent(np.arange(0, 31, 1), 'acneFrequency')
        self.resistance = ctrl.Antecedent(np.arange(0, 101, 1), 'externalFactors')
        self.skin_type = ctrl.Consequent(np.arange(0, 11, 1), 'skinType', defuzzify_method='mom')  # bisection, mom, lom

        # Definiowanie zbiorow rozmytych i funkcji przynaleznosci
        self.acne_frequency['v-rarely'] = fuzz.trapmf(self.acne_frequency.universe, [0, 0, 3.333, 6.667])
        self.acne_frequency['rarely'] = fuzz.trapmf(self.acne_frequency.universe, [3.333, 6.667, 10, 13.33])
        self.acne_frequency['sometimes'] = fuzz.trapmf(self.acne_frequency.universe, [10, 13.33, 16.67, 20])
        self.acne_frequency['often'] = fuzz.trapmf(self.acne_frequency.universe, [16.67, 20, 23.33, 26.67])
        self.acne_frequency['v-often'] = fuzz.trapmf(self.acne_frequency.universe, [23.33, 26.67, 30, 30])

        self.resistance['small'] = fuzz.trapmf(self.resistance.universe, [0, 0, 25, 37.5])
        self.resistance['medium'] = fuzz.trapmf(self.resistance.universe, [25, 37.5, 62.5, 75])
        self.resistance['large'] = fuzz.trapmf(self.resistance.universe, [62.5, 75, 100, 100])

        self.skin_type['dry'] = fuzz.trimf(self.skin_type.universe, [0, 0, 0])
        self.skin_type['mixed'] = fuzz.trimf(self.skin_type.universe, [5, 5, 5])
        self.skin_type['oily'] = fuzz.trimf(self.skin_type.universe, [10, 10, 10])

        # Definiowanie regul
        rule1 = ctrl.Rule(self.acne_frequency['v-rarely'] & self.resistance['small'], self.skin_type['dry'])
        rule2 = ctrl.Rule(self.acne_frequency['v-rarely'] & self.resistance['medium'], self.skin_type['dry'])
        rule3 = ctrl.Rule(self.acne_frequency['v-rarely'] & self.resistance['large'], self.skin_type['mixed'])
        rule4 = ctrl.Rule(self.acne_frequency['rarely'] & self.resistance['small'], self.skin_type['dry'])
        rule5 = ctrl.Rule(self.acne_frequency['rarely'] & self.resistance['medium'], self.skin_type['mixed'])
        rule6 = ctrl.Rule(self.acne_frequency['rarely'] & self.resistance['large'], self.skin_type['mixed'])
        rule7 = ctrl.Rule(self.acne_frequency['sometimes'] & self.resistance['small'], self.skin_type['dry'])
        rule8 = ctrl.Rule(self.acne_frequency['sometimes'] & self.resistance['medium'], self.skin_type['mixed'])
        rule9 = ctrl.Rule(self.acne_frequency['sometimes'] & self.resistance['large'], self.skin_type['oily'])
        rule10 = ctrl.Rule(self.acne_frequency['often'] & self.resistance['small'], self.skin_type['dry'])
        rule11 = ctrl.Rule(self.acne_frequency['often'] & self.resistance['medium'], self.skin_type['mixed'])
        rule12 = ctrl.Rule(self.acne_frequency['often'] & self.resistance['large'], self.skin_type['oily'])
        rule13 = ctrl.Rule(self.acne_frequency['v-often'] & self.resistance['small'], self.skin_type['mixed'])
        rule14 = ctrl.Rule(self.acne_frequency['v-often'] & self.resistance['medium'], self.skin_type['oily'])
        rule15 = ctrl.Rule(self.acne_frequency['v-often'] & self.resistance['large'], self.skin_type['oily'])

        # Tworzenie systemu sterowania
        self.baking_ctrl = ctrl.ControlSystem(
            [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15])
        self.braking_ctrl_simulation = ctrl.ControlSystemSimulation(self.baking_ctrl)

        # Przypisanie wartosci wejsciowych i symulacja
        input_value_acneFrequency = input1
        input_value_resistance = input2
        self.braking_ctrl_simulation.input['acneFrequency'] = input_value_acneFrequency
        self.braking_ctrl_simulation.input['externalFactors'] = input_value_resistance

        # Wywolanie sterowania
        self.braking_ctrl_simulation.compute()

        # Wyswietlenie wynikow
        output_value = self.braking_ctrl_simulation.output['skinType']
        print(output_value)

        return output_value

    def view_plots(self):
        #self.acne_frequency.view()
        #plt.show()
        #self.resistance.view()
        #plt.show()
        #self.skin_type.view()
        #plt.show()
        self.acne_frequency.view(sim=self.braking_ctrl_simulation)
        plt.show()
        self.resistance.view(sim=self.braking_ctrl_simulation)
        plt.show()
        self.skin_type.view(sim=self.braking_ctrl_simulation)
        plt.show()



myFuzzy = FuzzyModel()
myFuzzy.perform_fuzzy_logic(0, 30)
#myFuzzy.view_plots()