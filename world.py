#!/usr/bin/env python
# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# from turtlesim_enacter import TurtleSimEnacter # requires ROS
import random

import resources
from turtlepy_enacter import TurtlePyEnacter

# from Agent5 import Agent5
# from OsoyooCarEnacter import OsoyooCarEnacter

########## Class agent fournite au début
from turtlesim_enacter import TurtleSimEnacter


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        self._action = 0
        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = 0
        return self._action


###########################################
# AGENT 1   ##############################
class Agent1:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        # Action 0 par défaut
        self._action = 0
        # Il anticipe 0 au début pour une action 0
        self.anticipated_outcome = 0
        # compteur pour mésurer son ennui et pour qu'il change d'action
        self.compute_ennui = 0
        # Aprés combien de temps il commence a s'annyer
        self.seuil_enui = 4
        # Un mémoire pour bien anticiper ses actions
        # Rempli de cette maniere par défaut et ca sera mis a jour a chaque fois
        self.anticipation_memory = {}
        self.anticipation_memory[0] = 0
        self.anticipation_memory[1] = 1

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """

        self.MAJ_anticipation(self.anticipated_outcome == outcome)
        # TODO: Implement the agent's decision mechanism
        self.choose_action()
        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = self.anticipation_memory[self._action]
        # MAJ DE SES ANTICIPATIONS

        self.compute_ennui += 1
        return self._action

    def choose_action(self):
        if self.compute_ennui == 0:
            pass
        elif self.compute_ennui % self.seuil_enui == 0:
            self._action = self.get_inverse(self._action)

    def get_inverse(self, action):
        if action == 0:
            return 1
        else:
            return 0

    def MAJ_anticipation(self, bool):
        if bool:
            pass
        # On change la valeur de l'anticipation si c'est faux
        else:
            self.anticipation_memory[self._action] = self.get_inverse(self.anticipation_memory[self._action])


class Agent2:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        # Action 0 par défaut
        self._action = 0
        # Il anticipe 0 au début pour une action 0
        self.anticipated_outcome = 0
        # compteur pour mésurer son ennui et pour qu'il change d'action
        self.compute_ennui = 0
        # Aprés combien de temps il commence a s'annyer
        self.seuil_enui = 4
        # Un mémoire pour bien anticiper ses actions
        # Rempli de cette maniere par défaut et ca sera mis a jour a chaque fois
        self.anticipation_memory = {}
        self.anticipation_memory[0] = 0
        self.anticipation_memory[1] = 1

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """

        # MAJ DE SES ANTICIPATIONS
        self.MAJ_anticipation(self.anticipated_outcome == outcome)
        # TODO: Implement the agent's decision mechanism
        self.set_action_valeur_positif()
        self.check_ennui()
        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = self.anticipation_memory[self._action]

        self.compute_ennui += 1
        return self._action

    def check_ennui(self):

        if self.compute_ennui == 0:
            pass
        elif self.compute_ennui % self.seuil_enui == 0:
            self._action = self.get_inverse(self._action)

    def set_action_valeur_positif(self):
        if 0 < self.hedonist_table[self._action][self.anticipation_memory[self._action]]:
            pass
        else:
            inverse = self.get_inverse(self._action)
            if (0 < self.hedonist_table[inverse][self.anticipation_memory[inverse]]):
                self._action = inverse

    def get_inverse(self, action):
        if action == 0:
            return 1
        else:
            return 0

    def MAJ_anticipation(self, bool):
        if bool:
            pass
        # On change la valeur de l'anticipation si c'est faux
        else:
            self.anticipation_memory[self._action] = self.get_inverse(self.anticipation_memory[self._action])


class Agent3:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        # Action 0 par défaut
        self._action = 0
        # Il anticipe 0 au début pour une action 0
        self.anticipated_outcome = 0
        # compteur pour mésurer son ennui et pour qu'il change d'action
        self.compute_ennui = 0
        # Aprés combien de temps il commence a s'annyer
        self.seuil_enui = 4
        # Un mémoire pour bien anticiper ses actions
        # Rempli de cette maniere par défaut et ca sera mis a jour a chaque fois
        self.anticipation_memory = {}
        self.anticipation_memory[0] = 0
        self.anticipation_memory[1] = 0
        self.anticipation_memory[2] = 0
        self.possible_actions = [0, 1, 2]

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """

        # MAJ DE SES ANTICIPATIONS
        self.MAJ_anticipation(self.anticipated_outcome == outcome, outcome)
        # TODO: Implement the agent's decision mechanism
        self.set_action_valeur_positif()
        self.check_ennui()
        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = self.anticipation_memory[self._action]

        self.compute_ennui += 1
        return self._action

    def check_ennui(self):

        if self.compute_ennui == 0:
            pass
        elif self.compute_ennui % self.seuil_enui == 0:
            self._action = self.change_action(self._action)

    def set_action_valeur_positif(self):
        founded = False
        for i in self.possible_actions:
            if 0 < self.hedonist_table[i][self.anticipation_memory[i]]:
                self._action = i
                founded = True
        if not founded:
            self._action = random.randint(0, 2)

    def change_action(self, action):
        new_action = random.randint(0, 2)
        while (new_action == action):
            new_action = random.randint(0, 2)
        return new_action

    def MAJ_anticipation(self, bool, outcome):
        if bool:
            pass
        # On change la valeur de l'anticipation si c'est faux
        else:
            self.anticipation_memory[self._action] = outcome


class Agent4:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        # Action 0 par défaut
        self._action = 0
        # Il anticipe 0 au début pour une action 0
        self.anticipated_outcome = 0
        # compteur pour mésurer son ennui et pour qu'il change d'action
        self.compute_ennui = 0
        # Aprés combien de temps il commence a s'annyer
        self.seuil_enui = 4
        # Un mémoire pour bien anticiper ses actions
        # Rempli de cette maniere par défaut et ca sera mis a jour a chaque fois
        self.anticipation_memory = {}
        self.anticipation_memory[0] = 0
        self.anticipation_memory[1] = 0
        self.anticipation_memory[2] = 0
        self.possible_actions = [0, 1, 2]
        self.Interactions = None

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        # On stocke ce qu'on a fait dans les etapes d'avant
        if self.compute_ennui == 1:
            self.Interactions = resources.Interaction(self._action, outcome, self.hedonist_table[self._action][outcome])

        # MAJ DE SES ANTICIPATIONS
        self.MAJ_anticipation(self.anticipated_outcome == outcome, outcome)
        # TODO: Implement the agent's decision mechanism
        self.set_action_valeur_positif()
        #self.check_ennui()
        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = self.anticipation_memory[self._action]

        self.compute_ennui += 1
        self.Interactions.create_or_retrieve(self._action, outcome, self.hedonist_table[self._action][outcome])
        return self._action

    # def check_ennui(self):
    #
    #     if self.compute_ennui == 0:
    #         pass
    #     elif self.compute_ennui % self.seuil_enui == 0:
    #         self._action = self.change_action(self._action)

    def set_action_valeur_positif(self):
        founded = False
        if self.Interactions.interaction_list[-1].valence < 0:
            for i in self.possible_actions:
                if i != self._action:
                    if 0 < self.hedonist_table[i][self.anticipation_memory[i]]:
                        self._action = i
                        founded = True
                    if not founded:
                        self._action = self.change_action(self, self.action)
        else:
            pass

    def change_action(self, action):
        new_action = random.randint(0, 2)
        while (new_action == action):
            new_action = random.randint(0, 2)
        return new_action

    def MAJ_anticipation(self, bool, outcome):
        if bool:
            pass
        # On change la valeur de l'anticipation si c'est faux
        else:
            self.anticipation_memory[self._action] = outcome


class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """

    def outcome(self, action):
        # return int(input("entre 0 1 ou 2"))
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """

    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


class Environment3:
    """ Environment 3 yields outcome 1 only when the agent alternates actions 0 and 1 """

    def __init__(self):
        """ Initializing Environment3 """
        self.previous_action = 0

    def outcome(self, action):
        _outcome = 1
        if action == self.previous_action:
            _outcome = 0
        self.previous_action = action
        return _outcome


# TODO Define the hedonist valance of interactions (action, outcome)
# hedonist_table = [[-1, 1], [-1, 1]]
hedonist_table = [[-1, 1], [1, -1]]
# TODO Choose an agent
a = Agent2(hedonist_table)
# a = Agent5(hedonist_table)
# TODO Choose an environment
# e = Environment1()
# e = Environment1()
# e = Environment3()
e = TurtleSimEnacter()
# e = TurtlePyEnacter()
# e = OsoyooCarEnacter()

if __name__ == '__main__':
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(70):
        action = a.action(outcome)
        outcome = e.outcome(action)
