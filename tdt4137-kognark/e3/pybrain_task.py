import sys
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(1, 1)

ds.addSample((1,), (1,))
ds.addSample((2,), (2,))
ds.addSample((3,), (3,))
ds.addSample((4,), (4,))
ds.addSample((5,), (5,))
ds.addSample((6,), (6,))
ds.addSample((7,), (7,))
ds.addSample((8,), (8,))

hidden_layers = int(sys.argv[1])
print "Using %d hidden layers" % hidden_layers

net = buildNetwork(1, hidden_layers, 1, hiddenclass=TanhLayer, bias=True)
trainer = BackpropTrainer(net, ds)

print "Start training"
err = trainer.trainUntilConvergence(verbose=False, 
									validationProportion=0.15, 
									maxEpochs=1000, 
									continueEpochs=10)

#print err
print "Finished training"

print "Test function f(x)=x"
for i in range(1, 9):
	print "f(%d) = %f" % (i, net.activate((i, )))


print "f(%i) = %f" % (2, net.activate((2, )))
print "f(%d) = %f" % (-8, net.activate((-8, )))
print "f(%f) = %f" % (-0.234, net.activate((-0.234, )))
print "f(%d) = %f" % (1765345, net.activate((1765345, )))
print "f(%d) = %f" % (-34534, net.activate((-34534, )))

