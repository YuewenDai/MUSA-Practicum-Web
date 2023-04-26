****R Studio Server on Google Cloud****

1. Configure a virtual machine instance (Ubuntu OS) on Google Cloud.
    
    Step 1.1. Create a Google Cloud Project: Sign in to **[Google Cloud Console](https://console.cloud.google.com/)** and create a project.
    
    Step 1.2. Create a firewall rule: Create a firewall rule in the Google Cloud Compute Engine by navigating to the ‘Firewall rules’ under ‘Menu’ > ‘Networking’. Configure the following settings:
    
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a10657df-daf8-4d16-ac8b-4b0014ad69c6/Untitled.png)
    
    Step 1.3. Create a Virtual Machine Instance: Set up a new virtual machine on Google Cloud by navigating to ‘VM Instances’ under ‘Menu’ > ‘Compute Engine’.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2831901c-c644-4d58-b566-480e196096d6/Untitled.png)
    
    Step 1.4. Virtual Machine Configurations: Give a name to the new VM instance (ex: “rstudio”) and choose a zone that’s close to the zone of operation to reduce the network latency. Since R stores all of its working datasets in memory, try to give the VM instance as much memory as we can afford. Under “OS images”, choose one of the latest versions of Ubuntu that supports the OpenSSL 1.0. R Studio Server connects always through an unsecured HTTP connection. 
    
    Therefore, under Firewall, “Allow HTTP traffic”. Lastly, click “Create” to launch the instance.
    
2. Install R and R Studio Server on the Virtual Machine.
    
    Step 2.1. SSH Connection: Click on “SSH” next to the new instance from Google Compute Engine’s VM instances window. This will launch the command prompt.
    
    Step 2.2. Update apt: Update apt to make sure that we have the latest packages to use with Ubuntu.
    
    ```
    sudo apt-get update
    sudo apt-get upgrade
    ```
    
    Step 2.3. Install R and R Studio Server:
    
    ```
    sudo apt-get install r-base r-base-dev
    ```
    
    Check out the latest version of the **[RStudio Server](https://rstudio.com/products/rstudio/download-server/debian-ubuntu/)** before running the following lines of code. Install all the supporting packages:
    
    ```
    sudo apt-get install gdebi-core
    wgethttps://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.5019-amd64.deb
    sudo gdebi rstudio-server-1.2.5019-amd64.deb
    sudo apt-get install libcurl4-openssl-dev libssl-dev libxml2-dev
    
    ```
    
3. Create users and groups.
    
    Step 3.1. Create a group: Creating a group (ex: “marketing”) will make it easier to manage shared folders and files with the team.
    
    ```
    sudo addgroup rstudio-user
    ```
    
    Step 3.2. Create a master user: The whole idea behind creating a master user is that while colleagues and peers will join or leave us, the “master user” would remain to own all the shared files.
    
    ```
    sudo adduser master
    ```
    
    Step 3.3. Create the shared folder:
    
    ```
    cd /home/master
    sudo mkdir shared_folder
    sudo chown -R master:rstudio-user shared_folder/
    sudo chmod -R 770 shared_folder/
    ```
    
    Step 3.4. Add users and link them to a shared folder: Here I am adding Steve as an example to the recently created “marketing” group. Steve’s home folder has been linked to the ‘master user’s shared folder.
    
    ```
    sudo adduser steve
    sudo gpasswd -a steve rstudio-user
    su - steve
    ln -s /home/master/shared_folder /home/steve/shared_folder
    ```
    
4. Schedule and run R scripts using the cronR package.
    
    Install cronR package to generate the task scheduler in R Studio Server. Use the add-in to automate any scripts in the virtual machine instance.
    

```
install.packages("cronR")
install.packages("shinyFiles")
```

**Tips for selecting vm type:** 

1. check the quota limits for your account:
2. Select machine type on purpose
3. Make sure to monitor the running time for account
4. Install special dependency for spatial R packages
    
    ```
    sudo apt-get update
    sudo apt-get install gdal-bin libfontconfig1-dev libharfbuzz-dev libfribidi-dev 
    libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev
    libudunits2-dev libgdal-dev
    sudo apt install cmake
    
    ```
    
5. Understand the folding path of R and R studio for version control. Check the Rsession running status via SHH when you can not get access to the Rstudio
    
    ```
    sudo rstudio-server status
    ```
    
6. Check the storage space for your machine: Sometimes you upload too many files to your machine and you might not be able to save the result of your prediction. You can add an additional disk for storage but that will not speed up your calculation
    
    ```r
    $ lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda      8:0    0   10G  0 disk
    └─sda1   8:1    0   10G  0 part /
    sdb      8:16   0  100G  0 disk
    └─sdb1   8:17   0  100G  0 part /mnt/newdisk
    ```
    
7. It is possible to immigrant your machine between projects. Make use of the machine image and [Snapshot](https://cloud.google.com/compute/docs/disks/snapshot-best-practices)
