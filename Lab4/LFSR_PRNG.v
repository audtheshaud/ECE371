module LFSR_PRNG (
    input wire clk, // Create input clk wire
    input wire rst, // Create input reset wire
    output reg [2:0] out // Create output 3 bit register out
);
    reg [6:0] data_reg; // Create 7 bit regsiter data_reg
    wire feedback; // Create feedback wire

    // Feedback polynomial: x^6 XOR x^5 XOR 1
    assign feedback = data_reg[6] ^ data_reg[5] ^ 1'b1;
	initial begin
	// Assign the data_reg LSB to 1, the seed has to be set to produce a Psuedo random number
	data_reg = 7'b0000001; 
	end

	always @(posedge clk or negedge rst) begin
		if (!rst) begin
			// Left shift the data_reg by 1
			data_reg = data_reg << 1;
			// Concatenate the data_reg with the feedback produced by the XOR gate
			data_reg = {data_reg[6:1],feedback};
	 	end
	 	// Output the data_reg bits 2, 4, and 6
		out <= {data_reg[6],data_reg[4],data_reg[2]};
	end 
endmodule
