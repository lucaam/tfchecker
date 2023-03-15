# TestFlight Checker

Simple Python script that you can use to check free slots in a beta you want.

## Description

This Python script can send you a message on Telegram via a Bot (you already created) when a free slot is free. The beta link to TestFlight is sent in the message.

This is an private script made public without any attention to code, style, efficency etc.

## Getting Started

### Dependencies

* Telegram
* Working Telegram Bot (you already sent a message to the bot to start it)
* Telegram Bot Token
* Your chat ID
* Python 3.10
* PIP
* Linux/Mac (Windows if you run on Docker)
or
* Docker - if you want to use it

### Installing

```
git clone https://github.com/lucaam/tfchecker.git
cd tfchecker
python3 -m venv venv
mv renameme.env .env
vim .env
# setup your variables and save your file ":wq!"
pip -r requirements.txt
chmod +x run.sh
```

or (if you want to use Docker)

```
git clone https://github.com/lucaam/tfchecker.git
cd tfchecker
mv renameme.env .env
vim .env
# setup your variables and save your file ":wq!"
chmod +x run-docker.sh
```

### Executing program


```
./run.sh
```
or (if you folowed the Docker steps)

```
./run-docker.sh
```

## Authors

<a href="https://github.com/lucaam/tfchecker/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=lucaam/tfchecker" />
</a>

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Similar projects (I found after my work unfortunately)

* [testflight-watcher](https://github.com/jacopo-jtestflight-watcher)
* [scriptable-testflight-watcher](https://github.com/colin273/scriptable-testflight-watcher)