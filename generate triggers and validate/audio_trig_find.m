%% check sound triggers and find events

%% import
sound_dir = 'C:\Users\Richard Naar\Documents\dok\TARU\MDT 21\sounds';
addpath(sound_dir)

% Import the file
newData1 = importdata('11111.wav');

% Create new variables in the base workspace from those fields
vars = fieldnames(newData1);
for i = 1:length(vars)
    assignin('base', vars{i}, newData1.(vars{i}));
end
data = newData1.data;
fs = newData1.fs;

%% Double check trigger files

fdat = abs(fft(data)).^2;
% hz = 0:1/0.5:fs/2;
% plot(hz(2:end), fdat(2:length(hz)) )
plot(fdat)
%% Find events in waveforms recorded during the experiment

%% Import 2

raw_dir = 'C:\Users\Richard Naar\Documents\dok\TARU\MDT 21\muud\sounds';
addpath(raw_dir)
% Import the file
newData1 = importdata('test1.wav');

% Create new variables in the base workspace from those fields.
vars = fieldnames(newData1);
for i = 1:length(vars)
    assignin('base', vars{i}, newData1.(vars{i}));
end
data = newData1.data;
fs = newData1.fs;

%% Find events

event = abs(data)>0.1;
for i = 1:length(event)
    if event(i) > 0
        event(i+1:i+fs) = 0;
    end
end

eindx = find(event);

plot(data)
hold on
plot(event, 'r')
%% plot event markers and waveforms on the same plot
hz = 0:1:fs/2;

for ii = 1:length(eindx)
    data1 = data(eindx(ii):eindx(ii)+fs/20);
%     plot(data1)
    fdat = abs(fft(data1)).^2;
%     plot(fdat(2:length(hz)) )
    plot(fdat)
    pause()
end

