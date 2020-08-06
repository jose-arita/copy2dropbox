# Copy2Dropbox

Basic program for copy local folder and files to dropbox.

### Installation

Copy2Dropbox requires python 3.5+.

Clone the project.

```sh
$ git clone https://github.com/jose-arita/copy2dropbox.git
$ cd copy2dropbox
```

Create and activate python virtual environment and then install requirements.

```sh
(env)$ pip install -r requirements.txt
```

Copy `.env.example` file.

```sh
$ cp .env.example .env
```

Edit `.env` file.

```sh
DROPBOX_TOKEN=my_dropbox_token
LOCAL_DIR=/my/local/folder/path
DROPBOX_DIR=/my/destination/dropbox/folder
#set on for show proccess logs otherwise off
DEBUG=on
```
\*Obtain dropbox token  instructions [here](https://www.iperiusbackup.net/en/create-dropbox-app-get-authentication-token/).

Now run the program.

```sh
(env)$ python copy2dropbox.py
```

License
----

MIT
