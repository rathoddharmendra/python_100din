### Important learning notes

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPyuDjp7MR54frNziP9erEnW2xO63Glpgsgz9hr2w7po rathoddharmendra.business@gmail.com

her way of talking
slow thinking -- structurtally down to - breaking down
result oriented

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 3:
            return func(*args, **kwargs)
        else:
            abort(403)
    return wrapper


    Shers-MacBook-Air:~ mac_dee$ DD_API_KEY=d3e944c23a4c66b204ad27cd42266bde DD_SITE="datadoghq.eu" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_mac_os.sh)"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 19506  100 19506    0     0   178k      0 --:--:-- --:--:-- --:--:--  179k
Warning: DD_AGENT_MAJOR_VERSION not set. Installing Agent version 7 by default.

* Downloading datadog-agent
Password:
######################################################################### 100.0%

* Installing datadog-agent, you might be asked for your sudo password...

    - Mounting the DMG installer...

    - Unpacking and copying files (this usually takes about a minute) ...

    - Unmounting the DMG installer ...

* Restarting the Agent...



Your Agent is running properly. It will continue to run in the
background and submit metrics to Datadog.

You can check the agent status using the "datadog-agent status" command
or by opening the webui using the "datadog-agent launch-gui" command.


If you ever want to stop the Agent, please use the Datadog Agent App or
the launchctl command. It will start automatically at login.