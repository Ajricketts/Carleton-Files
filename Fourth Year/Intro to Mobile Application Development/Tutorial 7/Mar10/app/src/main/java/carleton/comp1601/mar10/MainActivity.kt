package carleton.comp1601.mar10

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var myMessage: TextView
    private var count = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        myMessage = findViewById(R.id.myMessage)
    }

    fun myButtonPressed(v: View) {
        count++
        myMessage.text = "You clicked $count times."
    }
}
