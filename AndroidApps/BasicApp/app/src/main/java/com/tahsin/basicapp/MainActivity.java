package com.tahsin.basicapp;

import androidx.appcompat.app.AppCompatActivity;
import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Scanner;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void onBtnClick(View view) {
        EditText email = findViewById(R.id.email);
        EditText pass = findViewById(R.id.password);
        if (email.getText().toString().equals("mail4tahsin@gmail.com") && pass.getText().toString().equals("skyout123")) {
            Toast.makeText(this, "Login Information Correct", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Login Information Incorrect", Toast.LENGTH_SHORT).show();
        }
    }
}