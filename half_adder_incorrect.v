module half_adder(
    input a,
    input b,
    output sum,
    output carry
);

reg sum, carry;

always @(a) begin
    sum = a ^ b;
    carry = a & b;
end

initial begin
    $display("Half adder instantiated");
end

endmodule

