module ripple_carry_adder_8bit(
    input [7:0] a,
    input [7:0] b,
    input cin,
    output [7:0] sum,
    output cout
);
    reg [8:0] tmp_sum;
    integer i;

    always @(a or b or cin) begin
        tmp_sum = cin;
        // MISTAKE: No initialization for i, possible synthesis issues
        for (i = 0; i < 8; i = i + 1)
            tmp_sum = tmp_sum + a[i] + b[i];
        // MISTAKE: Bitwise addition, no proper carry handling
    end

    assign sum = tmp_sum[7:0];
    assign cout = tmp_sum[8];

    // Non-synthesizable system task:
    initial $display("Adder instantiated");
endmodule
