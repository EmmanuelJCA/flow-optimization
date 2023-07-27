from modules.utils import getTrafficFlow, collect_date_range
import datetime as dt

def main():
    date_range = collect_date_range()
    start_date = date_range["start_date"]
    simulation_date = date_range["start_date"]
    end_date = date_range["end_date"]
    n_score = 0
    s_score = 0

    print("\nResultados de la simulacion por hora trascurrida:")
    while end_date >= simulation_date:
        traffic_flow_north = getTrafficFlow("Norte", simulation_date)
        traffic_flow_south = getTrafficFlow("Sur", simulation_date)
        # print(f"\nfecha y hora: {dt.datetime.strftime(simulation_date, '%d-%m-%Y %H:%M')}")
        # print(f"norte: {traffic_flow_north}")
        # print(f"sur: {traffic_flow_south}")
        if traffic_flow_north > traffic_flow_south:
            n_score+=1
        else:
            s_score+=1
        if simulation_date.hour == 22: 
            simulation_date = simulation_date + dt.timedelta(hours=8)
        else:
            simulation_date = simulation_date + dt.timedelta(hours=1)
    
    print(f"norte: {n_score}")
    print(f"sur: {s_score}")
        


main()