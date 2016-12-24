'use strict';

var gulp       = require('gulp'),
    rollup     = require('gulp-rollup'),
    sourcemaps = require('gulp-sourcemaps'),
    babel = require('gulp-babel'),
    // sass = require('gulp-sass'),
    uglify = require('gulp-uglify'),
    pump = require('pump'),
    nodeResolve = require('rollup-plugin-node-resolve'),
    spawn = require('child_process').spawn;

const static_path = './static/app';
let rollupOpts = {
  entry: './assets/js/main.js',
  allowRealFiles: true,
  context: 'window',
  plugins: [
    nodeResolve({
     // use "jsnext:main" if possible
     // – see https://github.com/rollup/rollup/wiki/jsnext:main
     jsnext: true,  // Default: false

     // use "main" field or index.js, even if it's not an ES6 module
     // (needs to be converted from CommonJS to ES6
     // – see https://github.com/rollup/rollup-plugin-commonjs
     main: true,  // Default: true

     // if there's something your bundle requires that you DON'T
     // want to include, add it to 'skip'. Local and relative imports
     // can be skipped by giving the full filepath. E.g.,
     // `path.resolve('src/relative-dependency.js')`
    //  skip: [ 'some-big-dependency' ],  // Default: []

     // some package.json files have a `browser` field which
     // specifies alternative files to load for people bundling
     // for the browser. If that's you, use this option, otherwise
     // pkg.browser will be ignored
     browser: true,  // Default: false

     // not all files you want to resolve are .js files
     extensions: [ '.js', '.json' ],  // Default: ['.js']

     // whether to prefer built-in modules (e.g. `fs`, `path`) or
     // local ones with the same names
    //  preferBuiltins: false  // Default: true

   })
  ]
};

gulp.task('scripts', () => {
  pump([
    gulp.src('./assets/**/*.js'),
    rollup(rollupOpts),
    babel({
      presets: ['es2015']
    }),
    uglify(),
    gulp.dest(`${static_path}`)
  ])

})

gulp.task('fonts', () => {
  gulp.src([
    './node_modules/bootstrap-sass/assets/fonts/bootstrap/*',
    './node_modules/font-awesome/fonts/*'
  ])
  .pipe(gulp.dest(`${static_path}/fonts`))
})

// gulp.task('sass', () => {
//  return gulp.src('./assets/scss/**/*.scss')
//   // .pipe(sourcemaps.init())
//   .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
//   // .pipe(sourcemaps.write())
//   .pipe(gulp.dest(`${static_path}`));
// })

gulp.task('django', () => {
  const runserver = spawn('./env/bin/python', ['manage.py', 'runserver'], { stdio: 'inherit', stderr: 'inherit' });
})

gulp.task('watch', ['scripts', 'fonts', 'django'], () => {
  gulp.watch('assets/js/**/*.js', ['scripts'])
  // gulp.watch('assets/scss/**/*.scss', ['sass'])
})

gulp.task('build', ['scripts', 'fonts'])
