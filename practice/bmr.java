
import java.awt.*;


import javax.swing.*;
import java.awt.Font;
import java.awt.event.ActionEvent;


public class bmrGui extends JFrame {

	public static double calculate_BMR(String gender, double weight, double height, int age) {
        if (gender.equalsIgnoreCase("male")) {
            return 88.36 + (13.4 * weight) + (4.8 * height) + (5.7 * age);
        } else if (gender.equalsIgnoreCase("female")) {
            return 447.6 + (9.2 * weight) + (3.1 * height) + (4.3 * age);
        } else {
            throw new IllegalArgumentException("Invalid gender. Use 'male' or 'female'.");
        }
    }

	public static void main(String[] args) {
		 new bmrGui();
		
	}

	
	JTextField weightfield ,heightfield ,Agetext;
	JLabel height_label , weight_label , resultLabel;
	JRadioButton male , female;
	public bmrGui() {
		getContentPane().setFont(new Font("Tahoma", Font.BOLD, 15));
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(700, 700);
		setTitle("BMR calculator ");
		getContentPane().setLayout(null);
		
		
		JLabel lblNewLabel = new JLabel("BMR CALCULATOR");
		lblNewLabel.setFont(new Font("Century Schoolbook", Font.BOLD, 30));
		lblNewLabel.setBounds(167, 11, 340, 60);
		getContentPane().add(lblNewLabel);
		
		height_label= new JLabel("Height (m) :");
	    height_label.setFont(new Font("Tahoma", Font.PLAIN, 15));
	    getContentPane().add(height_label);
	    height_label.setBounds(87, 108, 100, 30);
	    heightfield = new JTextField();
	    heightfield.setBounds(180 , 110 , 100 , 30);
	    getContentPane().add(heightfield);
	    
	    weight_label= new JLabel("Weight (kg) :");
	    weight_label.setFont(new Font("Tahoma", Font.PLAIN, 15));
	    getContentPane().add(weight_label);
	    weight_label.setBounds(290, 108, 100, 30);
	    weightfield = new JTextField();
	    weightfield.setBounds(389 , 110 , 100 , 30);
	    getContentPane().add(weightfield);

	    JButton CalculateButton= new JButton("Calculate");
	    CalculateButton.setForeground(Color.DARK_GRAY);
	    CalculateButton.setBackground(Color.CYAN);
	    CalculateButton.setBounds(87 , 279 ,100 ,46);
	    getContentPane().add(CalculateButton);
	    
	    resultLabel = new JLabel("");
	    resultLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
	    resultLabel.setBounds(87, 442, 438, 30);
	    getContentPane().add(resultLabel);

	    male= new JRadioButton("Male");
	    male.setSize(70, 46);
	    male.setLocation(180, 217);
	    female= new JRadioButton("female");
	    female.setSize(107, 46);
	    female.setLocation(252, 217);
	    ButtonGroup g1=new ButtonGroup();
	    g1.add(male);
	    g1.add(female);

	    //add(g1);
	    getContentPane().add(male);
	    getContentPane().add(female);
	    
	    JLabel GenderLabel = new JLabel("Gender");
	    GenderLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
	    GenderLabel.setBounds(87, 218, 70, 40);
	    getContentPane().add(GenderLabel);
	    
	    JLabel AgeLabel = new JLabel("Age :");
	    AgeLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
	    AgeLabel.setBounds(87, 166, 62, 30);
	    getContentPane().add(AgeLabel);
	    
	    JTextArea textArea = new JTextArea();
	    textArea.setBounds(87, 457, 5, 22);
	    getContentPane().add(textArea);
	    
	    AgeText = new JTextField();
	    AgeText.setBounds(180, 168, 100, 30);
	    getContentPane().add(AgeText);
	    AgeText.setColumns(10);
	    
	    CalculateButton.addActionListener(new ActionListener()
	    		{
	    	        @Override
	    	        public void actionPerformed(ActionEvent e)
	    	        {
	    	        	CalculateBMR();
	    	        }
	    	
	    		});

		
	    setVisible(true);
	}
	
	public void CalculateBMR()
	  {
	    try {
	        double weight = Double.parseDouble(weightfield.getText());
	        double height = Double.parseDouble(heightfield.getText());
	        int age=Int.parseInt(AgeText.getText());
	       // String gender= GenderLabel.getText();
	        double bmr_val = calculate_BMR("male",weight, height, age);
	        //System.out.println("weight :"+weight+ "height :"+ height);
	       // String category = getCategory(bmi_val);
	        resultLabel.setText("Your BMI is : " + bmr_val );
	        
	    } catch (NumberFormatException ex) {
	        JOptionPane.showMessageDialog(this, "Please enter valid numbers!", "Error", JOptionPane.ERROR_MESSAGE);
	    }
	  }

}
