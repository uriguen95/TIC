%% Borrar campo de trabajo y ventana de comandos
clc
clear all

canal = 1229695 %Identidad canal
Read = 'WF2MKRVV5GXIP0NB' %Llave de acceso a lectura

%%
data = thingSpeakRead(canal,'ReadKey',Read,'Fields',[1,2,3,4],'Numminutes',5,'OutputFormat','TimeTable')
%% Grafica Campo 1 - Temperatura
[dustData1,Timestamps1]=thingSpeakRead(canal,'ReadKey',Read,'Fields',1,'NumPoints',3000);
plot(Timestamps1,dustData1);
grid
xlabel('Tiempo (s)');
ylabel('Temperatura ºC');
title('Temperatura');
%% Grafica Campo 2 - Presion
[dustData2,Timestamps2]=thingSpeakRead(canal,'ReadKey',Read,'Fields',2,'NumPoints',3000);
plot(Timestamps2,dustData2);
grid
xlabel('Tiempo (s)');
ylabel('Presion (Pa)');
title('Presion Atmosferica');
%% Grafica Campo 3 - Altitud
[dustData3,Timestamps3]=thingSpeakRead(canal,'ReadKey',Read,'Fields',3,'NumPoints',3000);
plot(Timestamps3,dustData3);
grid
xlabel('Tiempo (s)');
ylabel('Altura (m)');
title('Altitud');
%% Grafica Campo 4 - Presion a nivel del mar
[dustData4,Timestamps4]=thingSpeakRead(canal,'ReadKey',Read,'Fields',4,'NumPoints',3000);
plot(Timestamps4,dustData4);
grid
xlabel('Tiempo (s)');
ylabel('Presion (Pa)');
title('Presion nivel del Mar');
