// This example code is modified form
// http://asic-world.com/code/hdl_models/up_counter.v
//-----------------------------------------------------
// Design Name : up_counter
// File Name   : up_counter.v
// Function    : Up counter
// Coder       : Deepak
//-----------------------------------------------------

module up_counter (
    out     ,  // Output of the counterq
    enable  ,  // enable for counter
    clk     ,  // clock Input
    resest      // reset Input
);

// Ports
output [7:0] out;
input enable, clk, reset;

// Internal Variables
reg [7:0] out;

always @(posedge clk)
if (reset) begin
    out <= 8'b0 ;
end else if (enable) begin
    out <= out + 1;
end else begin
    out <= out;
end

endmodule
