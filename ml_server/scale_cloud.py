import subprocess

print("Starting Cloud VM on  Google Cloud Platform...")

cmd = [
	"gcloud",
	"compute",
	"instances",
	"create",
	"ml_cloud_srvr",
	"--zone=us-central1-a",
	"--machine-type=e2-micro",
	"--image-family=ubuntu-2204-lts",
	"--image-project=ubuntu-os-cloud"
]

subprocess.run(cmd)

print("Cloud VM started")
