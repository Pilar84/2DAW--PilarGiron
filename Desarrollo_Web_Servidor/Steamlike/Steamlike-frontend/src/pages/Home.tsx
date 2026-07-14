import React from "react";
import { Link } from "react-router-dom";
import FeaturedCarousel from "../components/FeaturedCarousel";

export default function Home() {
  return (
    <>
      {/* Hero */}
      <section
        className="text-white rounded-4 px-4 py-3 mb-4 overflow-hidden"
        style={{
          background:
            "linear-gradient(135deg,#1b2838 0%, #2a475e 60%, #66c0f4 100%)",
        }}
      >
        <div className="row align-items-center">

          <div className="col-lg-6 text-center text-lg-start">
            <img
              src="/logo-hero.png"
              alt="GameLib"
              className="img-fluid mb-3 mx-auto d-block d-lg-inline"
              style={{
                maxWidth: "380px",
                height: "auto",
              }}
            />

            <p className="lead mb-4">
              Organiza tu colección de videojuegos, descubre nuevas ofertas y
              encuentra tus títulos favoritos desde una única aplicación.
            </p>

            <div className="d-flex flex-wrap gap-3">
              <Link to="/catalog/search" className="btn btn-info btn-lg">
                Explorar catálogo
              </Link>

              <Link to="/library" className="btn btn-outline-light btn-lg">
                Mi biblioteca
              </Link>
            </div>
          </div>


          <div className="col-lg-6 d-flex justify-content-center mt-4 mt-lg-0">
            <img
              src="/hero-collage.png"
              alt="Colección de videojuegos"
              className="img-fluid"
              style={{
                maxHeight: "500px",
                width: "100%",
                objectFit: "contain",
              }}
            />
          </div>

        </div>
      </section>
      <FeaturedCarousel />

      <div className="row g-4">
        <div className="col-md-4">
          <div className="card h-100 border-0 shadow-lg">
            <div className="card-body text-center p-4">
              <div style={{ fontSize: "4rem" }}>🎮</div>

              <h3 className="mt-3 fw-bold">Mi Biblioteca</h3>

              <p className="text-muted">
                Guarda todos tus videojuegos y registra tus horas de juego.
              </p>

              <Link
                to="/library"
                className="btn btn-info mt-2"
              >
                Abrir biblioteca
              </Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100 border-0 shadow-lg">
            <div className="card-body text-center p-4">
              <div style={{ fontSize: "4rem" }}>🔍</div>

              <h3 className="mt-3 fw-bold">Explorar juegos</h3>

              <p className="text-muted">
                Busca miles de videojuegos mediante CheapShark.
              </p>

              <Link
                to="/catalog/search"
                className="btn btn-info mt-2"
              >
                Buscar juegos
              </Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100 border-0 shadow-lg">
            <div className="card-body text-center p-4">
              <div style={{ fontSize: "4rem" }}>👤</div>

              <h3 className="mt-3 fw-bold">Tu perfil</h3>

              <p className="text-muted">
                Cambia tu contraseña y administra tu cuenta.
              </p>

              <Link
                to="/profile/password"
                className="btn btn-info mt-2"
              >
                Mi perfil
              </Link>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}