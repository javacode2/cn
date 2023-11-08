#Setup a FTP over TCP connection
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

$ns at 1.0 “$ftp start”
$ns at 124.0 “$ftp stop”

# next procedure gets two arguments: the name of the
# tcp source node, will be called here “tcp”,
# and the name of output file.

proc plotWindow {tcpSource file} {
global ns
set time 0.1
set now [$ns now]
set cwnd [$tcpSource set cwnd_]
set wnd [$tcpSource set window_]
puts $file “$now $cwnd”
$ns at [expr $now+$time] “plotWindow $tcpSource $file” }
$ns at 0.1 “plotWindow $tcp $winfile”

$ns at 125.0 “finish”
$ns run