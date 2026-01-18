## **1. Introduction to Wireshark**
Wireshark captures network packets in real-time, allowing users to inspect the details of network communications.  
**Key Features:**  
- Inspect live network traffic  
- Filter packets based on IP, protocol, or port  
- Analyze protocols at multiple layers (Ethernet → IP → TCP/UDP → Application)  
- Detect network problems and potential security threats  
- Visualize traffic patterns via graphs and statistics  

**Use Cases:**  
- Network troubleshooting (slow networks, dropped packets)  
- Security analysis (malware, suspicious traffic)  
- Learning protocols and network behavior  
- Debugging applications  

---

## **2. Installing and Setting Up Wireshark**
1. Download from [wireshark.org](https://www.wireshark.org/)  
2. Install and ensure **WinPcap/Npcap** is installed (required for packet capture)  
3. Open Wireshark → choose the correct **network interface**:  
   - **Wi-Fi / Ethernet**: Select the interface you want to capture traffic from  
   - **Promiscuous Mode**: Captures all packets on the network, not just packets addressed to your device  
4. **Hubs vs. Switches:**  
   - Hub: Broadcasts all traffic → easy to capture everything  
   - Switch: Sends traffic only to intended devices → harder to see full traffic  
5. **Wireless Capture:** Requires a Wi-Fi card supporting **monitor mode**  

---

## **3. Capturing Packets**
### **Starting Capture**
- Click your interface → Start Capture  
- Packets appear in **real-time** as they pass through the network  

### **Capture Options**
- Limit number of packets, capture duration, or file size  
- Use **capture filters** to capture only relevant packets  
  - Example: `tcp`, `udp`, `port 80`, `host 192.168.1.10`  

### **Stopping Capture**
- Click **Stop** when enough packets are captured  

### **Saving Captures**
- Save captures as `.pcap` or `.pcapng` for analysis later  

---

## **4. Viewing and Understanding Packets**
Wireshark interface has **three main panes**:  

1. **Packet List Pane:** Shows all captured packets (time, source, destination, protocol)  
2. **Packet Details Pane:** Expand each packet to see headers (Ethernet → IP → TCP/UDP → Application layer)  
3. **Packet Bytes Pane:** Shows raw data in hexadecimal  

**Tips:**  
- Right-click → **Follow TCP/UDP Stream** to see the full conversation  
- Expand protocol layers to see detailed info (flags, sequence numbers, options)  

---

## **5. Filters**
Filters allow you to focus on packets of interest.  

### **Capture Filters**
Applied **before capturing**:  
- `tcp` → Only TCP traffic  
- `udp` → Only UDP traffic  
- `host 192.168.1.10` → Only packets to/from this IP  

### **Display Filters**
Applied **after capture**:  
| Filter | Purpose |
|--------|---------|
| `tcp` | Show TCP packets only |
| `udp` | Show UDP packets only |
| `http` | Show HTTP requests/responses |
| `dns` | Show DNS queries/responses |
| `icmp` | Show ping requests/replies |
| `tcp.analysis.retransmission` | Show TCP retransmissions |
| `tcp.analysis.duplicate_ack` | Show duplicate ACKs |
| `ip.addr == 192.168.1.10` | Show packets from/to specific IP |
| `tcp.port == 443` | Show HTTPS traffic only |
| `!ip.addr == 192.168.1.10` | Exclude a specific IP |

**Dynamic Filters / Expressions:**  
- Combine filters: `ip.src == 192.168.1.10 && tcp.port == 80` → HTTP traffic from a device  
- Negation: `!` → exclude traffic  

---

## **6. Sorting, Searching, and Stream Following**
- **Sorting:** Click on column headers to sort by time, source, destination, protocol, etc.  
- **Searching:** Ctrl+F → search packet by content, protocol, or field  
- **Streams:** Right-click packet → **Follow TCP/UDP Stream** → see full conversation  

---

## **7. Packet Analysis**
### **7.1 Latency**
- **Definition:** Time taken for a packet to travel from source → destination  
- **How to analyze:**  
  - Right-click packet → **Time Delta (ΔT)**  
  - Statistics → I/O Graphs → visualize response times  

### **7.2 Packet Loss**
- Look for **retransmissions** (Wireshark highlights in red)  
- Display Filter: `tcp.analysis.retransmission`  
- Duplicate ACKs indicate packet loss or network congestion: `tcp.analysis.duplicate_ack`  

### **7.3 Retransmissions**
- TCP resends packets when ACK not received  
- Red packets in Wireshark indicate retransmissions  

### **7.4 Duplicate Acknowledgments**
- Multiple ACKs for the same packet indicate packet loss or reordering  
- Filter: `tcp.analysis.duplicate_ack`  

---

## **8. Expert Analysis**
Wireshark can automatically highlight errors and warnings:  
- **Expert Information:** View TCP errors, protocol issues, malformed packets  
- **Suspicious Traffic:** Look for unusual IPs, repeated failed connections, unknown protocols  

**Filters for suspicious traffic:**  
- `tcp.port == 23` → Telnet traffic  
- `smb` → SMB traffic  
- `ip.src != 192.168.1.0/24` → Outside network IP  

---

## **9. Statistics and Visualization**
Wireshark provides detailed analysis tools:

| Feature | Use |
|---------|-----|
| **Summary** | Total packets, capture duration, data rate |
| **Protocol Hierarchy** | Percentage of each protocol in capture |
| **Endpoints** | Devices communicating on network |
| **Conversations** | Communication between IPs and ports |
| **I/O Graphs** | Traffic trends over time, latency spikes |
| **GeoIP Mapping** | Map packet source/destination globally |

---

## **10. Saving and Exporting**
- Save entire capture or selected packets (`File → Export Packet Dissections`)  
- Export objects from protocols (HTTP files, images)  
- Use **tshark** (CLI) for automated captures, splitting files, merging captures, and generating statistics  

---

## **11. Advanced Features**
### **11.1 VoIP Analysis**
- Locate conversations, RTP streams, and ladder diagrams  
- Extract audio from RTP streams  
- VoIP Statistics → call durations, codecs  

### **11.2 Command-line Capture**
- `tshark` → capture traffic without GUI  
- Can split or merge capture files  
- Apply filters during capture  

### **11.3 GeoIP**
- Identify packet origin geographically  
- Map communication endpoints  

---

## **12. Coloring Rules in Wireshark**

### **1. What are Coloring Rules?**
Coloring Rules allow you to **highlight packets with different colors** based on conditions (display filters).  
This makes it easier to **spot errors, retransmissions, specific protocols, or suspicious traffic** at a glance.

---

### **2. How to Use Coloring Rules**
1. Go to **View → Coloring Rules…** in Wireshark.  
2. You will see default rules, e.g.:  
   - Red: TCP retransmissions (`tcp.analysis.retransmission`)  
   - Light Blue: DNS queries/responses (`dns`)  
   - Green: TCP ACKs (`tcp.flags.ack == 1`)  
3. To **add a new rule**:  
   - Click **+**  
   - Enter a **Display Filter**, e.g., `http.response.code == 404`  
   - Pick **Foreground** and **Background colors**  
   - Click **OK** to save  

---

### **3. Useful Default Coloring Rules**

| Color | Display Filter | Purpose / Use Case |
|-------|----------------|-----------------|
| Red | `tcp.analysis.retransmission` | Retransmitted packets (possible packet loss) |
| Light Red / Pink | `tcp.analysis.duplicate_ack` | Duplicate ACKs (network congestion) |
| Light Blue | `dns` | DNS queries/responses |
| Dark Green | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | TCP SYN packets (new connections) |
| Green | `tcp.flags.ack == 1` | ACK packets |
| Orange | `http` | HTTP requests/responses |
| Purple | `icmp` | Ping requests/replies |

---

### **4. Tips for Using Coloring Rules**
- Use **bright/warm colors** (red, orange) for errors or suspicious packets  
- Use **cool colors** (green, blue) for normal or expected traffic  
- Combine with **display filters** to focus on packets of interest  
- Enhances **visual troubleshooting** and makes reports more professional  
- Great for quickly identifying latency, packet loss, or HTTP errors  

---

### **5. Example Use Case**
For Marvel Task 5:  
- Apply **red for retransmissions** → instantly see lost packets  
- Apply **orange for HTTP errors** → quickly locate failed requests  
- Apply **green for ACKs** → monitor normal traffic flow  

This allows you to **analyze network issues visually** without reading every packet in detail.

---- 

## **13. Conclusion**
Wireshark is a powerful network analysis tool. Using it, you can:  
- Capture and inspect all network packets  
- Diagnose latency, packet loss, and retransmissions  
- Identify security threats and suspicious traffic  
- Visualize traffic with graphs and statistics  
- Analyze protocols end-to-end from Ethernet to Application layer  


