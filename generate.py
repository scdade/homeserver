import binascii;

hInnerscript = open("innerscript.py",'r');
data = hInnerscript.read();

base64=binascii.b2a_base64(data.encode('ascii'));
base64=base64.decode('ascii');
base64=base64.replace("\n","");
base64=base64.replace("\r","");

module = open("17778.in.hsl",'r');
moduledata = module.read();

moduledata.encode('ascii');
moduledata=moduledata.replace("%INNERSCRIPT%",str(base64))
fullscript=moduledata;

outFile = open("17778.hsl",'w');
outFile.write(fullscript);
outFile.close()


module = open("17779.in.hsl",'r');
moduledata = module.read();

moduledata.encode('ascii');
moduledata=moduledata.replace("%INNERSCRIPT%",str(base64))
fullscript=moduledata;

outFile = open("17779.hsl",'w');
outFile.write(fullscript);
outFile.close()


module = open("17780.in.hsl",'r');
moduledata = module.read();

moduledata.encode('ascii');
moduledata=moduledata.replace("%INNERSCRIPT%",str(base64))
fullscript=moduledata;

outFile = open("17780.hsl",'w');
outFile.write(fullscript);
outFile.close()
