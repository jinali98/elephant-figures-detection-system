def setVideoConfig(capture):
    capture.set(3, 240);
    capture.set(4, 380);


def dnnConfig(net):
    net.setInputSize(320,320);
    net.setInputScale(1.0/127.5);
    net.setInputMean((127.5, 127.5, 127.5));
    net.setInputSwapRB(True);