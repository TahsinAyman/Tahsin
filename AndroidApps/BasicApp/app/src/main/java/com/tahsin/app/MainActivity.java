package com.tahsin.app;

import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends androidx.appcompat.app.AppCompatActivity {
    private List<User> users = new ArrayList<>();

    @Override
    protected void onCreate(android.os.Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onLoginBtnClick(View view) {
        try {
            EditText email = findViewById(R.id.email);
            EditText pass = findViewById(R.id.password);
            User user = new User(email.getText().toString(), pass.getText().toString());
            for (User u : users) {
                if (user.getEmail().equals(u.getEmail()) &&
                        user.getPassword().equals(u.getPassword())) {
                    Toast.makeText(this, "login Succesfully", Toast.LENGTH_SHORT).show();
                }
            }
        } catch (Exception e) {
            Toast.makeText(this, "Login Error!", Toast.LENGTH_SHORT).show();
        }
    }

    public void onRegisterBtnClick(View view) {
        try {
            EditText email = findViewById(R.id.email);
            EditText pass = findViewById(R.id.password);
            User user = new User(email.getText().toString(), pass.getText().toString());
            email.setText("");
            pass.setText("");
            this.users.add(user);

            Toast.makeText(this, "Succesfull Register", Toast.LENGTH_SHORT).show();
        } catch (Exception e) {
            Toast.makeText(this, "Error! Register", Toast.LENGTH_SHORT).show();
        }
    }
}