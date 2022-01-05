from pathlib import Path

from loggibud.v1.data_conversion import to_tsplib_competition
from loggibud.v1.types import CVRPInstance

# Convert all files with less than upper_bound clients
upper_bound = 2000

def convert_file(instance_file: str):
    """Read a data file and converts into a TSPLIB format"""
    loggibud_instance = CVRPInstance.from_file(instance_file)
    tsplib_file_name = f"tsplib_data/{loggibud_instance.name}.vrp"

    if Path(tsplib_file_name).exists():
       print(f"File {loggibud_instance.name} already exists. Skipping")
       return

    print(f"Converting file {loggibud_instance.name}")

    print(f"Clients: {len(loggibud_instance.deliveries)}")
    if(len(loggibud_instance.deliveries) < upper_bound):
        print(instance_file,len(loggibud_instance.deliveries))
    
    tsplib_instance = to_tsplib_competition(loggibud_instance)
    with open(tsplib_file_name, "w") as f:
        tsplib_instance.write(f)


if __name__ == "__main__":
    path = Path("../data/cvrp-instances-1.0/")

    cnt = 0
    for instance_file in path.rglob("*.json"):
        convert_file(instance_file)

    print(cnt)