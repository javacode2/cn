set ns [new Simulator]
set node_(0) [$ns node]
set node_(1) [$ns node]
# Defining a transport agent for sending
set udp [new Agent/UDP]
# Attaching transport agent to sender node
$ns attach-agent $node_(0) $udp
# Defining a transport agent for receiving
set null [new Agent/Null]
# Attaching transport agent to receiver node
$ns attach-agent $node_(1) $null
#Connecting sending and receiving transport agents
$ns connect $udp $null
#Defining Application instance
set cbr [new Application/Traffic/CBR]
# Attaching transport agent to application agent
$cbr attach-agent $udp
#Packet size in bytes and interval in seconds definition
$cbr set packetSize_ 512
$cbr set interval_ 0.1
# data packet generation starting time
$ns at 1.0 "$cbr start"
# data packet generation ending time
$ns at 6.0 "$cbr stop"
where,
ns → Simulator instance
UDP → User datagram Protocol
CBR → Constant Bit Rate