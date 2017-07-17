from pgmpy.factors import TabularCPD
from pgmpy.models import BayesianModel


olympic_model = BayesianModel([('Genetics', 'OlympicTrials'),
                                ('Practice', 'OlympicTrials'),
                                ('OlympicTrials', 'Offer')])


genetics_cpd = TabularCPD (
            variable = 'Genetics',
            variable_card = 2,
            values = [[.2,.8]])

practice_cpd = TabularCPD (
            variable = 'Practice',
            variable_card = 2,
            values = [[.2,.8]])

offer_cpd = TabularCPD (
            variable = 'Offer',
            variable_card = 2,
            values = [[.95, .8, .5],
                    [.05, .2, .5]],
            evidence= ['OlympicTrials'],
            evidence_card = 3)

olympic_trials_cpd = TabularCPD(
            variable = 'OlympicTrials',
            variable_card = 3,
            values = [[.5, .8, .8, .9],
                        [.3, .15, .1, .08],
                        [.2, .05, .1, .02]],
            evidence= ['Genetics', 'Practice'],
            evidence_card=[2,2]

)


# Add the relationships to your models

olympic_model.add_cpds ( genetics_cpd, practice_cpd, offer_cpd, olympic_trials_cpd)

# Examine the graph structure
olympic_model.get_cpds()

# Find active trail nodes
olympic_model

