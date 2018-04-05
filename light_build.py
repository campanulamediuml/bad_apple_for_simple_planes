import make_beacon_matrix
fh = open('/Users/JingjingHe/Library/Application Support/unity.Jundroo.SimplePlanes/AircraftDesigns/bad_apple_test.xml','w')
fh.close()

# fh = open('/Users/JingjingHe/Library/Application Support/unity.Jundroo.SimplePlanes/AircraftDesigns/bad_apple.xml')
# print fh.read()
# fh.close()

fh = open('/Users/JingjingHe/Library/Application Support/unity.Jundroo.SimplePlanes/AircraftDesigns/bad_apple_test.xml','a')

xml_header = '''<?xml version="1.0" encoding="utf-8"?>
<Aircraft name="bad_apple_test" url="" theme="Default" size="150,1.645,100" boundsMin="-75,1.733354,-50" xmlVersion="6">
  <Assembly>
    <Parts>
      <Part id="4" partType="Fuselage-Body-1" position="0,31.84585,3.33786E-06" rotation="0,0,0" drag="392.6389,392.6389,15003.95,15003.95,343.7867,342.9735" materials="13" scale="50,1,40" massScale="1">
        <FuelTank.State fuel="0" capacity="0" />
        <Fuselage.State version="2" frontScale="2,2" rearScale="2,2" offset="0,0,2" deadWeight="0" buoyancy="1000" fuelPercentage="0" cornerTypes="0,0,0,0,0,0,0,0" />
      </Part>
      <Part id="5" partType="Cockpit-4" position="0,12.8465,3.33786E-06" rotation="0,0,0" drag="0,0,0,0,0,0" materials="7,0,1" scale="1,1,1" massScale="1">
        <Cockpit.State primaryCockpit="True" />
      </Part>'''
      
fh.write(xml_header)
count = 5
# x_0 = -43.75
y_0 = -19.5
for y in range(0,30):
    x_0 = 60
    for x in range(0,40):
        x_0 -= 1
        count += 1
        string = ''
        for i in make_beacon_matrix.result[count-6]:
          if len(str(i)) != 1:
            string = string + str(i)[:-1]+'.'+str(i)[-1]+','
          else:
            string = string + '0.'+str(i)+','
        light_program = string[:-1]
        
        position_light = '''<Part id="'''+str(count)+'''" partType="BeaconLight" position="'''+str(x_0)+''',2.733355,'''+str(y_0)+'''" rotation="0,0,0" drag="0,0,0.7739998,0.7739998,0.7739998,0.7739999" materials="14,0" scale="10,10,10" massScale="1">
        <BeaconLight.State activationGroup="1" designerBlinkProgram="Quick Blink" input="None" showHalo="false" blinkProgram="'''+str(light_program)+'''"/>
      </Part>\n'''
        fh.write(position_light)
    y_0 += 1
fh.write('</Parts>'+'\n'+'<Connections>\n')
fh.write('<Connection partA="5" partB="4" attachPointsA="1" attachPointsB="3" />\n')
for i in range(6,count+1):
    fh.write('<Connection partA="'+str(i)+'" partB="4" attachPointsA="0" attachPointsB="2" />\n')
fh.write('</Connections>\n<Bodies>\n<Body partIds="')
for i in range(6,count):
    fh.write(str(i)+',')
fh.write(str(count)+'" position="0,0,0" rotation="0,0,0" velocity="0,0,0" angularVelocity="0,0,0" />\n')
xml_tail = '''</Bodies>
  </Assembly>
  <Theme name="Custom">
    <Material color="E9E9E9" r="0.15" m="0.5" s="0.7" />
    <Material color="000000" r="0.3" m="0.5" s="0.83" />
    <Material color="001F7F" r="0.3" m="0.5" s="0.83" />
    <Material color="AA2A00" r="0.15" m="0.5" s="0.7" />
    <Material color="3F3F3F" r="0" m="0.65" s="0.08" />
    <Material color="5C0000" r="0" m="0.65" s="0.08" />
    <Material color="FFFFFF" r="0" m="0.65" s="0.08" />
    <Material color="FFF0F0" r="0" m="0.65" s="0.08" />
    <Material color="FF0F0F" r="0" m="0.65" s="0.08" />
    <Material color="AAAAAA" r="0" m="0.65" s="0.08" />
    <Material color="3F3F3F" r="0.15" m="0.5" s="0.7" />
    <Material color="ABABAB" r="0" m="0.65" s="0.08" />
    <Material color="446677" r="0" m="0.65" s="0.08" />
    <Material color="FF1143" r="0" m="0.65" s="0.08" />
    <Material color="FF6A12" r="0" m="0.65" s="0.08" />
    <Material color="000000" r="0" m="0.65" s="0.08" />
    <Material color="FFFFFF" r="0" m="0.65" s="0.08" />
    <Material color="1E1E1E" r="0" m="0.65" s="0.08" />
    <Material color="FFFFFF" r="0" m="0.65" s="0.08" />
  </Theme>
</Aircraft>'''
fh.write(xml_tail)
fh.close()




