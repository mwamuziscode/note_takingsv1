from notes.models.tag  import Category, Tag, Note
from faker import Faker
from django.contrib.auth.models import User


# CREATE TAGS AND CATEGORIES


# DELETE ALL TAGS AND CATEGORIES
# def deleteAllTags():
#     Tag.objects.all().delete()
#     return 'All Tags deleted successfully'

# def deleteAllCategories():
#     Category.objects.all().delete()
#     return 'All Categories deleted successfully'

# def deleteAllNotes():
#     Note.objects.all().delete()
#     return 'All Notes deleted successfully'


# deleteAllTags()
# deleteAllCategories()
# deleteAllNotes()




tags_data = [
    'Physics', 'QuantumMechanics', 'QuantumMechanics', 'QuantumMechanics', 'Physics', 
    'QuantumPhysics', 'WaveParticleDuality', 'QuantumTheory', 'QuantumState', 
    'SchrodingerEquation', 'QuantumSuperposition', 'WaveFunctionCollapse', 'QuantumEntanglement',
    'ProbabilityAmplitude', 'InterferencePattern', 'ScienceExplained', 'PhysicsLecture',
    'QuantumConcepts', 'SuperpositionPrinciple', 'QuantumExperiments', 'QuantumMeasurement',
    'QuantumInterference', 'QuantumDecoherence', 'QuantumInformation', 'QuantumComputing',
    'QuantumCryptography', 'QuantumTeleportation', 'QuantumErrorCorrection', 'QuantumAlgorithms',
    'QuantumSimulation', 'QuantumAnnealing', 'QuantumMachineLearning', 'QuantumInternet',
    'QuantumSensors', 'QuantumMetrology', 'QuantumImaging', 'QuantumOptics', 'QuantumElectronics',
    'QuantumMaterials', 'QuantumNanotechnology', 'QuantumBiology', 'QuantumChemistry',
    'QuantumPhysicsBooks', 'QuantumPhysicsVideos', 'QuantumPhysicsLectures', 'QuantumPhysicsExperiments',
    'QuantumPhysicsSimulations', 'QuantumPhysicsResearch', 'QuantumPhysicsNews', 'QuantumPhysicsHistory',
    'QuantumPhysicsPhilosophy', 'QuantumPhysicsEducation', 'QuantumPhysicsCareers',
    'QuantumPhysicsOrganizations', 'QuantumPhysicsConferences', 'QuantumPhysicsJournals',
    'QuantumPhysicsMagazines', 'QuantumPhysicsWebsites', 'QuantumPhysicsBlogs', 'QuantumPhysicsForums',
    'QuantumPhysicsSocialMedia', 'QuantumPhysicsPodcasts', 'QuantumPhysicsBooks', 'QuantumPhysicsVideos',
    'QuantumPhysicsLectures', 'QuantumPhysicsExperiments', 'QuantumPhysicsSimulations', 'QuantumPhysicsResearch',
    'QuantumPhysicsNews', 'QuantumPhysicsHistory', 'QuantumPhysicsPhilosophy', 'QuantumPhysicsEducation',
    'QuantumPhysicsCareers'
]

    # Create tags using the list
    for tag_name in tags_data:
        Tag.objects.create(name=tag_name)

    return 'All Tags created successfully'

createTag()