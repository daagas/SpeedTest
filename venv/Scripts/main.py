import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Download speed: {download} \nUpload speed: {upload}")