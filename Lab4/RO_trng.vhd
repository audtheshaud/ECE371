library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- The STD_LOGIC data type allows signals to represent the following states:
-- 'U' : Uninitialized (unknown value, default state before initialization)
-- 'X' : Forcing Unknown (conflicting or invalid logic)
-- '0' : Forcing 0 (strong logic low)
-- '1' : Forcing 1 (strong logic high)
-- 'Z' : High Impedance (tri-state, no driver on the signal)
-- 'W' : Weak Unknown (unknown value due to weak driving)
-- 'L' : Weak 0 (weak logic low)
-- 'H' : Weak 1 (weak logic high)
-- '-' : Don't care (used in simulation or synthesis to signify irrelevant value)
use IEEE.STD_LOGIC_UNSIGNED.ALL;
-- Enables arithmetic operations (ex: addition and subtraction) on STD_LOGIC_VECTOR data types

entity RO_TRNG is
    Port ( trn : out std_logic_vector(20 downto 0); -- 21 bit Totally Random Number
	   reset : in  std_logic; -- Resets the Ring Oscillators to their original seed
	   -- reset is set to pin_AA14 which is push-button[0]
	   sample: in std_logic; -- Controls the random output of the Ring Oscillators
	   -- sample is set to pin_AA15 which is push-button[1]
		clk : in  std_logic); -- Set to pin_AF14 A.K.A CLOCK_50
end entity RO_TRNG;

architecture Behavioral of RO_TRNG is
  signal ring    : std_logic_vector(20 downto 0):= "100101101011011101001"; -- 21 bit randomly picked seed for the original ring
  signal ring2   : std_logic_vector(20 downto 0):= "110101000110011101001"; -- 21 bit randomly picked seed for the second ring
  signal clk_int : std_logic; -- Initializtion of clk_int
  attribute KEEP : string; -- Defines KEEP as attribute of string type 
  attribute KEEP of ring : signal is "true"; -- Tells synthesis tool to not mangle (optimize by removal) the ring signal
  attribute KEEP of ring2 : signal is "true"; -- Tells synthesis tool to not mangle (optimize by removal) the ring2 signal

component iclk is
	port (
		iclk_clk       : out std_logic;        -- clk
		iclk_en_oscena : in  std_logic := 'X'  -- oscena
	);
end component iclk; 

begin
	u0 : component iclk
		port map (
			iclk_clk       => clk_int, -- Maps iclk_clk to the clk_int (Internal clock)
			iclk_en_oscena => '1'      -- Enables the oscillator
		);
  
  assert ring'length mod 2 = 1 report "Length of ring must be an odd number!" severity failure;
  assert ring2'length mod 2 = 1 report "Length of ring must be an odd number!" severity failure;
  -- Check to make sure the lengths are of odd length, otherwise display an error

  trn <= (ring xor ring2) when sample ='0'; -- When push-button[1] is pressed perform an xor on ring and ring2
  -- trn is mapped to LED[9:0], when push-button[1] is no longer pressed, trn's value is displayed on the LEDs
  
  process (clk_int,ring,reset) begin
  if reset='0' then -- If the reset signal is low
	  ring <= "100101101011011101001"; -- Set ring to the original seed
  else
	  if rising_edge(clk_int) then -- During the rising edge of the clock
		  for i in ring'range loop -- For each bit in ring
			 if i = ring'left then -- If the current bit i is equal to the MSB
				ring(i) <= not ring(0) after 1ns; -- Set the MSB to the inverse of the LSB
			 else
				ring(i)   <= not ring(i+1) after 1ns; -- Set the current bit i to the inverse of the next bit
			 end if;
		  end loop;
		  end if;
	end if;
  end process;
  
    process (clk,ring,reset) begin
  if reset='0' then -- If the reset signal is low
	  ring2 <= "110101000110011101001"; -- Set ring2 to the original seed
  else
	  if rising_edge(clk) then -- During the rising edge of the clock
		  for i in ring2'range loop -- For each bit in ring
			 if i = ring2'left then -- If the current bit i is equal to the MSB
				ring2(i) <= not ring2(0) after 1ns; -- Set the MSB to the inverse of the LSB
			 else
				ring2(i)   <= not ring2(i+1) after 1ns; -- Set the current bit i to the inverse of the next bit
			 end if;
		  end loop;
		  end if;
	end if;
  end process;

end Behavioral;
