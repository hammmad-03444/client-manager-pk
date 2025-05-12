import streamlit as st
from datetime import date
from client_manager import ClientManager,Client

#Initialize client manager and load existing client 
client_manager = ClientManager()
client_manager.load_from_file()

st.set_page_config(page_title="🧾 Freelance Client Manager", layout="centered")
st.title("🧾 Freelance Client Manager ")
st.markdown("Manage your local freelancing clients easily. Add , Track , and Mark Payments")

#sidebar navigation
st.sidebar.title("Navigation")
menu=st.sidebar.radio("Go to",["➕Add Client","📋View All Clients","❌View Unpaid Clients","✅Mark as Paid"])



# Add Client Form

if menu == "➕Add Client":
    st.header("Add New Client")
    with st.form("add_client_form"):
      name = st.text_input("👤 Client Name")
      contact = st.text_input("📞 Contact Info (Phone/WhatsApp)")
      project = st.text_input("📝 Project Name")
      deadline = st.date_input("📅 Deadline",min_value=date.today())
      amount = st.number_input("💰 Project Amount",min_value=0)
      submit_button = st.form_submit_button("Add Client")

      if submit_button and name and contact and project and amount and project:
         client=Client(name, contact, project,str(deadline) ,amount, project)
         client_manager.add_client(client)
         client_manager.save_to_file()
         st.success(f"Client {name} added successfully!")

elif menu == "📋View all clients":
   st.header("📋 View All Clients")
   clients=client_manager.get_all_clients()
   if not clients:
      st.write("No Clients Found")
   else:
      for client in clients:
         st.markdown(f"""
        ** Name:{client.name}**
        ** Contact:{client.contact}**
        ** Project:{client.project}**
        ** Deadline:{client.deadline}**
        ** Amount:{client.amount}**
        ** Paid:{'✅ Yes' if client.paid else '❌ No'}**
        ------
        """)
         
#view unpaid clients
elif menu == "❌View Unpaid Clients":
   st.header("❌Unpaid Clients")
   unpaid_clients=client_manager.get_unpaid_clients()
   if not unpaid_clients:
      st.write("No Unpaid Clients Found")
   for client in unpaid_clients:
      st.markdown("""
        **Name:** {client.name}  
        **Contact:** {client.contact}  
        **Project:** {client.project_details}  
        **Deadline:** {client.deadline}  
        **Amount:** PKR {client.amount}  
        **Paid:** ❌ No  
        ---
        """)
   
#update client status
elif menu == "✅Mark as Paid":
   st.header("✅Mark as Paid")
   unpaid_clients=client_manager.get_unpaid_clients()
   if not unpaid_clients:
      st.success("All clients are marked as paid.")
   else:
      client_names = [client.name for client in unpaid_clients]
      selected_names = st.selectbox("Select client to mark as paid", client_names)
      if st.button("Mark Paid"):
         client_manager.mark_as_paid(selected_names)
         client_manager.save_to_file()
         st.success(f"Client {selected_names} marked as paid.")
