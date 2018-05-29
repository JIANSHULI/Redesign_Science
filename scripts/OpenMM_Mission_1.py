from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
from Redesign_Science import DATA_PATH
import os

try:
    pdb = PDBFile('input.pdb')
    forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
except:
    pdb = PDBFile(os.path.join(DATA_PATH, '../examples/input.pdb'))
    forcefield = ForceField(DATA_PATH + '/../../simtk/openmm/app/data/amber14-all.xml', DATA_PATH + '/../../simtk/openmm/app/data/amber14/tip3pfb.xml')
        

system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
                                 nonbondedCutoff=1*nanometer, constraints=HBonds)
integrator = LangevinIntegrator(300*kelvin, 1/picosecond, 0.002*picoseconds)
simulation = Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)
simulation.minimizeEnergy()
simulation.reporters.append(PDBReporter(DATA_PATH + '/../examples/output.pdb', 1000))
simulation.reporters.append(StateDataReporter(stdout, 1000, step=True,
                                              potentialEnergy=True, temperature=True))
simulation.step(10000)