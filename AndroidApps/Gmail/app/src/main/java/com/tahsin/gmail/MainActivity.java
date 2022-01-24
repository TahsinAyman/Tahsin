package com.tahsin.gmail;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    @SuppressLint("SetTextI18n")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    @SuppressLint("SetTextI18n")
    public void onBtnClick(View view) {
        EditText firstName = findViewById(R.id.firstName);
        EditText lastName = findViewById(R.id.lastName);
        EditText email = findViewById(R.id.email);
        TextView showFirstName = findViewById(R.id.showFirstName);
        TextView showLastName = findViewById(R.id.showLastName);
        TextView showEmail = findViewById(R.id.showEmail);

        showFirstName.setText("First Name: " + firstName.getText().toString());
        showLastName.setText("Last Name: " + lastName.getText().toString());
        showEmail.setText("Email: " + email.getText().toString());
    }
}