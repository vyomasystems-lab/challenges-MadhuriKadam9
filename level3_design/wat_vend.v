module wat_vend(
    input clk,
    input rst,
    input [1:0]inp,
    output reg out
    );

parameter s0 = 2'b00;
parameter s1 = 2'b01;  //5 Rs state
parameter s2 = 2'b10;  //10 Rs state

reg [1:0]c_state,n_state;

always @(posedge clk)
begin
	if(rst==1)
	begin
	c_state=0;
	n_state=0;
	end
	else
	begin
	c_state=n_state;
	case(c_state)
	s0: if(inp==0)
		begin
		n_state=s0;
		out=0;
		end
		else if(inp==2'b01)
		begin
		n_state=s1;
		out=0;
		end
		else if(inp==2'b10)
		begin
		n_state=s2;
		out=0;
		end
		
	s1: if(inp==0)
		begin
		n_state=s0;
		out=0;
		end
		else if(inp==2'b01)
		begin
		n_state=s2;
		out=0;
		end
		else if(inp==2'b10)
		begin
		n_state=s0;
		out=1;
		end

	s2: if(inp==0)
		begin
		n_state=s0;
		out=0;
		end
		else if(inp==2'b01)
		begin
		n_state=s0;
		out=1;
		end
		else if(inp==2'b10)
		begin
		n_state=s0;
		out=1;
		end
		
	endcase
	
		
	end
end
endmodule
