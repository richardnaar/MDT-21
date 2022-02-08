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
hz = 0:1/0.1:fs/2;
plot(hz(2:end), fdat(2:length(hz)) )
% plot(fdat)
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

plot(data(eindx(4):eindx(4)+fs/9))

plot(data)
hold on
plot(event, 'r')
%% find triggers
trig = [110, 333, 554, 784, 1046]; 
% trig(1) == start/end % trig(2) == fb/brush % trig(3) == dif/easy
% trig(4:5) % out: 10 == less, 01 == same, 11 == greater

%% plot event markers and waveforms on the same plot
dur = fs/1;
hz = 0:fs/dur:fs-1;
% hz = 0:1/0.5:fs/2;

for ii = 1:length(eindx)
    data1 = data(eindx(ii):eindx(ii)+dur);
%     plot(data1)
   fdat = abs(fft(data1)).^2/length(data1);
    plot(hz(2:length(hz)/2), fdat(2:length(hz)/2) )
%      plot(hz(2:length(hz)/2), fdat(2:length(hz)/2) )
%     plot(fdat)
%% find triggers

    raw_trig = find(abs(fdat(2:length(hz)/2))>0.2);
    event = zeros(1, length(raw_trig));
    for f_ind = 1:length(raw_trig)
        idx = dsearchn(trig', raw_trig(f_ind));
        if any(trig(idx) - raw_trig(f_ind) < 20) 
            event(f_ind) = trig(idx);
        end
    end
    event = unique(event);
    event_i = zeros(1, length(trig));
    for ei = 1:length(event)
        idx = dsearchn(trig', event(ei));
        event_i(idx) = 1;
    end

    if event_i(1)
        fprintf('start +')
    else
        fprintf('end +')
    end

    if event_i(2)
        fprintf('fb +')
    else
        fprintf('brush +')
    end

    if event_i(3)
        fprintf('dif +')
    else
        fprintf('easy +')
    end

    if sum(event_i(4:5)) == 2
        fprintf('greater\n')
    elseif event_i(4) == 1
        fprintf('less\n')
    elseif event_i(5) == 1
        fprintf('same\n')
    end

    pause()
end

