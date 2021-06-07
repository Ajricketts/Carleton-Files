package carleton.comp1601.picviewer2a

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.View
import android.widget.EditText
import android.widget.ImageView

val appName = "PicViewer2A"
val pics = arrayOf(R.drawable.kittens, R.drawable.roshi, R.drawable.roshi2)

class MainActivity : AppCompatActivity() {
    private lateinit var p: ImageView
    private var pic = R.drawable.kittens
    private var picIndex = 0
    private lateinit var rotationInput: EditText
    private lateinit var scaleInput: EditText
    private lateinit var pXInput: EditText
    private lateinit var pYInput: EditText

    val r = PicWatcher("rotation", 0F, ::updateImage)
    {r ->
        if (r > 720F) return@PicWatcher 720F
        if (r < 0F) return@PicWatcher 0F
        r
    }
    val s = PicWatcher("scale", 1F, ::updateImage)
    {s ->
        if (s > 5F) return@PicWatcher 5F
        if (s < 0) return@PicWatcher 0F
        s
    }
    val X = PicWatcher("X", 0F, ::updateImage, ::clamp_xy)
    val Y = PicWatcher("Y", 0F, ::updateImage, ::clamp_xy)

    fun clamp_xy(v: Float): Float {
        if (v > 1000F) return 1000F
        if (v < -1000F) return -1000F
        return v
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        if (savedInstanceState != null) {
            // do something
        }

        p = findViewById(R.id.mypic)

        rotationInput = findViewById(R.id.rotation)
        rotationInput.addTextChangedListener(r)

        scaleInput = findViewById(R.id.scale)
        scaleInput.addTextChangedListener(s)

        pXInput = findViewById(R.id.x)
        pXInput.addTextChangedListener(X)

        pYInput = findViewById(R.id.y)
        pYInput.addTextChangedListener(Y)

        updateImage()
        Log.d(appName, "Activity Created")
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        Log.d(appName, "State saved")
    }

    fun updateImage() {
        p.setImageResource(pic)
        p.setX(X.value)
        p.setY(Y.value)
        p.setRotation(r.value)
        p.setScaleX(s.value)
        p.setScaleY(s.value)
    }

    fun nextImage(v: View) {
        picIndex = (picIndex + 1) % pics.size
        pic = pics[picIndex]
        updateImage()
    }
}

class PicWatcher: TextWatcher {
    var value: Float
    var default_value: Float
    var name: String
    var update: () -> Unit
    var clamp: (Float) -> Float

    override fun afterTextChanged(s: Editable) {
        val new_value = s.toString().toFloatOrNull()

        if (new_value != null) {
            value = clamp(new_value)
            Log.d(appName, "Set ${name} to ${value}.")
        } else {
            value = default_value
            Log.d(appName, "Set ${name} to default value ${value}.")
        }

        update()
    }

    override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
    }

    override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
    }

    constructor(n: String, v: Float, u: () -> Unit, c: (Float) -> Float) {
        value = v
        default_value = v
        name = n
        update = u
        clamp = c
    }
}
