'use strict';

var gulp       = require('gulp'),
  rollup = require('rollup-stream'),
  source = require('vinyl-source-stream'),
  babel = require('rollup-plugin-babel'),
  uglify = require('rollup-plugin-uglify'),
  nodeResolve = require('rollup-plugin-node-resolve'),
  spawn = require('child_process').spawn;

const static_path = './static/app';

gulp.task('scripts', function() {
  return rollup({
    input: './assets/js/main.js',
    format: 'umd',
    context: 'window',
    plugins: [nodeResolve({
      jsnext: true,  // Default: false
      main: true,  // Default: true
      browser: true,  // Default: false
      extensions: [ '.js', '.json' ],  // Default: ['.js']
    }),
    babel({
      exclude: 'node_modules/**'
    }),
    uglify(),
    ]
  })
    .pipe(source('js/main.js'))
    .pipe(gulp.dest(static_path));
});

gulp.task('fonts', () => {
  gulp.src([
    './node_modules/bootstrap-sass/assets/fonts/bootstrap/*',
    './node_modules/font-awesome/fonts/*'
  ])
    .pipe(gulp.dest(`${static_path}/fonts`));
});

gulp.task('django', () => {
  const runserver = spawn('python', ['manage.py', 'runserver'], { stdio: 'inherit', stderr: 'inherit' });
});

gulp.task('watch', ['scripts', 'fonts', 'django'], () => {
  gulp.watch('assets/js/**/*.js', ['scripts']);
  // gulp.watch('assets/scss/**/*.scss', ['sass'])
});

gulp.task('build', ['scripts', 'fonts']);
