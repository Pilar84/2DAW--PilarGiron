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
        <div className="row align-items-center py-1">

          <div
            className="col-lg-6 d-flex flex-column align-items-center align-items-lg-start text-center text-lg-start"
            style={{ marginTop: "-50px" }}
          >            <img
              src="/logo-hero.png"
              alt="GameLib"
              className="img-fluid mb-3"
              style={{
                maxWidth: "320px",
                height: "auto",
              }}
            />
            <p className="lead mb-4">
              Organiza tu colección de videojuegos, descubre nuevas ofertas y
              encuentra tus títulos favoritos desde una única aplicación.
            </p>

            <div className="d-flex justify-content-center justify-content-lg-start gap-2">
              <Link
                to="/catalog/search"
                className="btn btn-info flex-fill flex-sm-grow-0"
              >
                Explorar catálogo
              </Link>

              <Link
                to="/library"
                className="btn btn-outline-light flex-fill flex-sm-grow-0"
              >
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

      <div className="row g-3 mt-1">
        <div className="col-md-4">
          <div className="card h-100 border-0 shadow-lg">
            <div className="card-body text-center p-3">
              <div style={{ fontSize: "3rem" }}>🎮</div>

              <h3 className="h4 mt-2 fw-bold">
                Mi Biblioteca
              </h3>

              <p className="text-muted mb-3">
                Guarda todos tus videojuegos y registra tus horas de juego.
              </p>

              <Link
                to="/library"
                className="btn btn-info btn-sm"
              >
                Abrir biblioteca
              </Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100 border-0 shadow-lg">
            <div className="card-body text-center p-3">
              <div style={{ fontSize: "3rem" }}>🔍</div>

              <h3 className="h4 mt-2 fw-bold">
                Explorar juegos
              </h3>

              <p className="text-muted mb-3">
                Busca miles de videojuegos mediante CheapShark.
              </p>

              <Link
                to="/catalog/search"
                className="btn btn-info btn-sm"
              >
                Buscar juegos
              </Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100 border-0 shadow-lg">
            <div className="card-body text-center p-3">
              <div style={{ fontSize: "3rem" }}>👤</div>

              <h3 className="h4 mt-2 fw-bold">
                Tu perfil
              </h3>

              <p className="text-muted mb-3">
                Cambia tu contraseña y administra tu cuenta.
              </p>

              <Link
                to="/profile/password"
                className="btn btn-info btn-sm"
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