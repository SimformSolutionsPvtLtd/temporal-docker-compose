from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/reset-workflow/")
def reset_workflow(workflow_id: str, run_id: str, reset_type: str = "FirstWorkflowTask"):
    cmd = [
        "tctl", "workflow", "reset",
        "--workflow_id", workflow_id,
        "--run_id", run_id,
        "--reset_type", reset_type,
        "--reason", "reset from API"
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {
        "stdout": result.stdout.decode(),
        "stderr": result.stderr.decode(),
        "returncode": result.returncode
    }
