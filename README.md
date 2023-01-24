# Tool.BackupMacPhotos

This tool is used to copy files from your Mac Photo Library to an external drive or folder.
Within this step it creates a new folder structure.

Keep in mind, I do not check for existing space or something else. This tool is running recursively through each folder.

I use this tool do handle backups of my photos on external drives with my common folder structure.

## Go running
```bash
main.py -i <inputFolder> -o <outputFolder>
```

Notes: 
- By default the Photos library is a file named `Photos Library.photoslibrary`
- It is located in `/Users/$user/Pictures` or  `~/Pictures`
- Output folder can be an external drive or what else


## Folder structure

```bash
--TargetFolder
----YEAR (2023)
------MONTH (01)
------MONTH (XX)
----YEAR (2022)
------MONTH (01)
------MONTH (02)
------MONTH (XX)
----YEAR (XXXX)
------MONTH (XX)
------MONTH (XX)
```


## Future stuff
1. Add progress bar
