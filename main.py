# main.py
import streamlit as st
import config
import sessionstate
import logic
import api
import frontend

# 1. Setup Page & State
st.set_page_config(**config.PAGE_CONFIG)
st.markdown(config.CUSTOM_CSS, unsafe_allow_html=True)
sessionstate.init_session_state()

st.title("⚛️ Quantum Logistics Pro")
if not st.session_state.optimized_route:
    st.info("👈 Please configure your stops in the sidebar and click RUN to start.")

# 2. Render Sidebar Inputs
start_loc, is_round_trip, mileage, fuel_price, go_btn = frontend.render_sidebar()

# 3. Main Application Logic
if go_btn:
    if not start_loc:
        st.error("⚠️ Please select a Start Location.")
    elif not st.session_state.stops_data:
        st.error("⚠️ Please add at least one stop.")
    else:
        with st.spinner("⚛️ Initializing Quantum Tunneling Simulation..."):
            
            st.session_state.is_round_trip_active = is_round_trip
            
            # --- CALL QUANTUM SOLVER ---
            # Logic returns the full ordered list. 
            # If round_trip=True, the last node in sorted_nodes is the Start Node.
            sorted_nodes, stats = logic.optimize_route_algo(
                start_loc, 
                st.session_state.stops_data, 
                round_trip=is_round_trip
            )
            
            # --- SPLIT PATH PROCESSING ---
            total_km = 0
            total_min = 0
            main_geo = []
            return_geo = []
            
            if is_round_trip:
                # Slice list: Main Trip = Start -> Last Stop
                # Return Trip = Last Stop -> Start
                
                # Everything up to the last stop (exclude the appended start node)
                main_segment = sorted_nodes[:-1] 
                
                # The return leg (Last Stop -> Appended Start Node)
                return_segment = [sorted_nodes[-2], sorted_nodes[-1]]
                
                # 1. Get Main Path (Blue)
                coords_main = [n['coords'] for n in main_segment]
                path_geo_main, km1, min1 = api.get_road_path(coords_main)
                
                # 2. Get Return Path (Red)
                coords_return = [n['coords'] for n in return_segment]
                path_geo_return, km2, min2 = api.get_road_path(coords_return)
                
                total_km = km1 + km2
                total_min = min1 + min2
                main_geo = path_geo_main if path_geo_main else coords_main
                return_geo = path_geo_return if path_geo_return else coords_return
                
            else:
                # Standard One-Way Trip
                coords_seq = [n['coords'] for n in sorted_nodes]
                path_geo, total_km, total_min = api.get_road_path(coords_seq)
                main_geo = path_geo if path_geo else coords_seq
                return_geo = None # No return leg
            
            # --- CALCULATE LOGISTICS METRICS ---
            total_fuel = total_km / mileage
            total_cost = total_fuel * fuel_price
            
            # --- UPDATE SESSION STATE ---
            st.session_state.route_metrics = {
                "dist": total_km,
                "time": total_min,
                "fuel": total_fuel,
                "cost": total_cost
            }
            
            # Store split geometries so Frontend can color them differently
            st.session_state.optimized_route = {
                "names": [n['name'] for n in sorted_nodes],
                "coords": [n['coords'] for n in sorted_nodes],
                "geo": main_geo,         # Blue Path
                "return_geo": return_geo # Red Dotted Path
            }
            
            # Store Quantum Analytics
            st.session_state.optimization_stats = stats
            
            st.rerun()

# 4. Render Results Dashboard
frontend.render_dashboard()
