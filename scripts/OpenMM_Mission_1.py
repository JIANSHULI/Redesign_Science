from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout

try:
    pdb = PDBFile('input.pdb')
    forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
except:
    try:
        pdb = PDBFile('/nfs/blender/data/jshu_li/anaconda3/envs/MD_Simulation/lib/python3.6/site-packages/openmm/examples/input.pdb')
        forcefield = ForceField('/nfs/blender/data/jshu_li/anaconda3/envs/MD_Simulation/lib/python3.6/site-packages/simtk/openmm/app/data/amber14-all.xml', 'amber14/tip3pfb.xml')
    except:
        pdb = PDBFile('/Users/JianshuLi/anaconda3/envs/MD_Simulation/lib/python3.6/site-packages/openmm/examples/input.pdb')
        

system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
                                 nonbondedCutoff=1*nanometer, constraints=HBonds)
integrator = LangevinIntegrator(300*kelvin, 1/picosecond, 0.002*picoseconds)
simulation = Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)
simulation.minimizeEnergy()
simulation.reporters.append(PDBReporter('output.pdb', 1000))
simulation.reporters.append(StateDataReporter(stdout, 1000, step=True,
                                              potentialEnergy=True, temperature=True))
simulation.step(10000)