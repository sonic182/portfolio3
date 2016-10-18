'use strict';

var gulp       = require('gulp'),
    rollup     = require('gulp-rollup'),
    sourcemaps = require('gulp-sourcemaps'),
    babel = require('gulp-babel'),
    sass = require('gulp-sass');

gulp.task('scripts', () => {
  gulp.src('./assets/**/*.js')
    // .pipe(sourcemaps.init())
      // transform the files here.
      .pipe(rollup({
        entry: './assets/js/main.js',
      }))
      .pipe(babel({
            presets: ['es2015']
        }))
    // .pipe(sourcemaps.write())
    .pipe(gulp.dest('./static'));
})

gulp.task('fonts', () => {
  gulp.src([
    './node_modules/bootstrap-sass/assets/fonts/bootstrap/*'
  ])
  .pipe(gulp.dest('./static/fonts'))
})

gulp.task('sass', function () {
 return gulp.src('./assets/scss/**/*.scss')
  // .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  // .pipe(sourcemaps.write())
  .pipe(gulp.dest('./static'));
})

gulp.task('watch', ['scripts', 'sass', 'fonts'], () => {
  gulp.watch('assets/js/**/*.js', ['scripts'])
  gulp.watch('assets/scss/**/*.scss', ['sass'])
})

gulp.task('build', ['scripts', 'sass', 'fonts'])
