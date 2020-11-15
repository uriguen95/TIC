%% Borrar campo de trabajo y ventana de comandos
clc
clear all

%https://www.mathworks.com/help/thingspeak/read-data-from-channel.html
%% Descargamos los datos de thingSpeak

%Identidades de cada canal
channelID_1 = 1229695;
channelID_2 = 1229725;

% Llaves de acceso a lectura
Read = 'WF2MKRVV5GXIP0NB';
Read2 = 'LNRTKEUVDTBH1BWH';

%Obtencion de datos
[data_1,timestamps_1] = thingSpeakRead(channelID_1,'ReadKey',Read,'NumPoints',300);
[data_2,timestamps_2] = thingSpeakRead(channelID_2,'ReadKey',Read2,'NumPoints',300);

%% Juntamos los datos de los dos canales
nData = 300;
tempData=[];
presData=[];
for i=1:nData
% Primera columna Presion (Field2), segunda columna Temperatura (Field1) pero se
% varia en cada ejecucion en funcion de los tipos de datos a analizar.
    presData = [presData; data_1(i,2); data_2(i,2)];
    tempData = [tempData; data_1(i,1); data_2(i,1)];
end
%% Realizar la correlacion
corrplot([presData,tempData],'varNames',{'P(Pa)', 'T(ºC)'});
