function [command] = relay()
    %RELAY Turns light on and off on command
    %   Relay sends the command to ThingSpeak to turn on light or off
    command = input('Would you like to turn the LED on or off? (enter "LED_ON" or "LED_OFF"): ', 's')
    if ~(strcmp(command,'LED_ON') | strcmp(command,'LED_OFF'))
        error('func must be either "LED_ON" or "LED_OFF"')  
    end

    % TalkBack app ID
    TalkBack_ID = '41122'; 
    % TalkBack command ID
    Command_ID = '21084180'; 
    % TalkBack app API key
    TalkBack_apikey = '4E2U6B7VRBGIOE6D'; 

    url =  strcat('https://api.thingspeak.com/talkbacks/',TalkBack_ID,'/commands.json');
    response = webwrite(url,'api_key',TalkBack_apikey,'command_string',command)

    if (strcmp(command,'LED_ON'))
        webwrite('https://api.thingspeak.com/update?api_key=BAENZAFXSV5BVZ2S&field4=1','1')
    end

    if (strcmp(command,'LED_OFF'))
        webwrite('https://api.thingspeak.com/update?api_key=BAENZAFXSV5BVZ2S&field4=0','0')
    end
end